from pyspark.sql import SparkSession, functions as f
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

KAFKA_SERVER = 'kafka:29092'
KAFKA_TOPIC = 'sales-topic'
USERS_PATH = '/datalake/trusted/users'
SALES_PATH = '/datalake/refined/grouped-sales'


def spark_session():
    spark = SparkSession.builder.getOrCreate()
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
    return df.withColumn('value', f.from_json(f.col('value').cast('string'), sales_schema()))


def process(df):
    return df.select('value.*') \
        .withColumn('product', f.struct('product.name', 'product.price', 'quantity')) \
        .withColumn('created_at', f.to_date(
            f.regexp_replace(f.col('created_at'), r'\s\d+:\d+:\d+', ''),
            'yyyy-MM-dd'
        )) \
        .withColumn('user', f.regexp_replace(f.col('user'), r'#', '')) \
        .groupBy('user', 'created_at') \
        .agg(
            f.collect_list(f.col('product')).alias('products'),
            f.sum('total').alias('total'),
            f.collect_set(f.col('source')).alias('sources')
        )\
        .withColumn('processed_at', f.current_date())


if __name__ == '__main__':
    spark = spark_session()
    try:
        df = spark.read \
            .format('kafka') \
            .option('kafka.bootstrap.servers', KAFKA_SERVER) \
            .option('subscribe', KAFKA_TOPIC) \
            .load()
        
        df = parse_msg(df)
        df.cache()
        df.printSchema()
        df.show()
        print(f'Records Found: {df.count()}')

        df = process(df)
        df.cache()
        df.printSchema()
        df.show()
        print(f'Records: {df.count()}')

        df.write \
            .mode('overwrite') \
            .partitionBy('user', 'created_at') \
            .parquet(SALES_PATH)

        df.unpersist()

    except Exception as ex:
        print(f'Unexpected Error! {ex}')
    finally:
        spark.stop()
