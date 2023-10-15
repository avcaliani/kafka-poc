from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, to_timestamp, current_timestamp
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

KAFKA_SERVER = 'kafka:29092'
KAFKA_TOPIC = 'sales-topic'
CHECKPOINT_PATH = '/datalake/checkpoint/spark-app/sales-topic/streaming'
USERS_PATH = '/datalake/trusted/users'
SALES_PATH = '/datalake/trusted/sales'


def spark_session():
    spark = SparkSession \
        .builder \
        .appName('sales-streaming') \
        .config('spark.sql.streaming.checkpointLocation', CHECKPOINT_PATH) \
        .getOrCreate()
    print(f'Spark Version: {spark.version}')
    return spark


def sales_schema():
    return StructType([
        StructField('user', StringType()),
        StructField('product', StructType([
            StructField('name', StringType()),
            StructField('price', DoubleType()),
        ])),
        StructField('quantity', IntegerType()),
        StructField('total', DoubleType()),
        StructField('created_at', StringType()),
        StructField('source', StringType())
    ])


def parse_msg(df):
    return df.withColumn('data', from_json(col('value').cast('string'), sales_schema())) \
        .select('data.*')


def process(df, users):
    return df.filter(col('user') != '#fake_user') \
        .withColumn('created_at', to_timestamp(col('created_at'), 'yyyy-MM-dd HH:mm:SS')) \
        .withColumn('processed_at', current_timestamp()) \
        .join(users, 'user', 'left')


def show(df):
    df.writeStream \
        .queryName('sales-console') \
        .trigger(processingTime='10 seconds') \
        .format('console') \
        .option('truncate', False) \
        .start()


def save_data(df, epoch_id):
    print(f'INFO: Persisting Batch {epoch_id}')
    df.cache()
    df.write \
        .mode('append') \
        .partitionBy('user') \
        .parquet(SALES_PATH)
    # If I had to save in another place like a database,
    # I should use this space to develop it.
    df.unpersist()


if __name__ == '__main__':
    spark = spark_session()
    try:
        df = spark.readStream \
            .format('kafka') \
            .option('kafka.bootstrap.servers', KAFKA_SERVER) \
            .option('subscribe', KAFKA_TOPIC) \
            .option('maxOffsetsPerTrigger', 20) \
            .load()

        users = spark.read.option('header', True).csv(USERS_PATH)
        df = parse_msg(df)
        df = process(df, users)

        df.printSchema()
        show(df)

        df.writeStream \
            .queryName('sales-persist') \
            .trigger(processingTime='5 seconds') \
            .foreachBatch(save_data) \
            .start()

        spark.streams.awaitAnyTermination()
    except Exception as ex:
        print(f'Unexpected Error! {ex}')
    finally:
        spark.stop()
