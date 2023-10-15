#!/bin/bash -xe
# @script       run.sh
# @author       Anthony Vilarim Caliani
# @contact      github.com/avcaliani
#
# @params
# 01 - Script Name
#
# @usage
# ./run.sh [ batch | streaming ]

spark-submit --master local \
    --name "sales-${1:-unknown}-$(date +%Y%m%d%H%M%S)" \
    --packages "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1" \
    --conf "spark.sql.sources.partitionOverwriteMode=dynamic" \
    "/app/src/$1.py"

exit 0
