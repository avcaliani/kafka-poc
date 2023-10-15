FROM python:3.8

ENV JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"

ENV SPARK_HOME="/opt/spark"
ENV SPARK_VERSION="3.1.1"
ENV HADOOP_VERSION="2.7"
ENV PATH="$SPARK_HOME/bin:$PATH"

ENV PYSPARK_PYTHON=python
ENV PATH="$SPARK_HOME/python:$PATH"

WORKDIR /opt

# Java
RUN echo "deb http://ftp.us.debian.org/debian sid main" >> /etc/apt/sources.list
RUN apt-get update && apt-get -y install gcc-8-base openjdk-11-jdk && apt-get -y autoremove

# Spark
ADD "https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz" .
RUN tar -xzf spark*.tgz && rm -f spark*.tgz && mv spark* spark

RUN touch /opt/spark/conf/log4j.properties
RUN echo 'log4j.rootLogger=ERROR, console\n\
\n\
# Console Appender\n\
log4j.appender.console=org.apache.log4j.ConsoleAppender\n\
log4j.appender.console.layout=org.apache.log4j.PatternLayout\n\
log4j.appender.console.layout.ConversionPattern=\u001b[m%d{yyyy/MM/dd HH:mm:ss} \u001b[36;1m%p\u001b[m [\u001b[32;1m%t\u001b[m] \u001b[34;1m%c{1}\u001b[m: %m%n\n\
\n\
# Logging Level\n\
log4j.logger.org.apache=ERROR\n\
log4j.logger.org.spark_project=ERROR\n\
log4j.logger.parquet=ERROR\n\
log4j.logger.org.apache.kafka=ERROR\n' >> /opt/spark/conf/log4j.properties

CMD tail -f /dev/null