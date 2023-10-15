#!/bin/bash -xe
# @script       kafka.sh
# @author       Anthony Vilarim Caliani
# @contact      github.com/avcaliani
#
# @description
# Utilities script for Apache Kafka.
#
# @params
# 01 - Topic Name
#
# @usage
# ./kafka.sh [ --create | --describe | --test-pub | --test-sub ] TOPIC_NAME

ZOOKEEPER_URL='zookeeper:2181'
for arg in "$@"
do
    case $arg in

        --create)
        docker-compose exec kafka kafka-topics --create \
            --topic "$2" \
            --partitions "1" \
            --replication-factor "1" \
            --if-not-exists \
            --zookeeper "$ZOOKEEPER_URL"
        shift; shift
        ;;

        --describe)
        docker-compose exec kafka kafka-topics --describe \
            --topic "$2" \
            --zookeeper "$ZOOKEEPER_URL"
        shift; shift
        ;;

        --test-pub)
        docker-compose exec kafka  \
            bash -c "seq 100 | kafka-console-producer --request-required-acks 1 --broker-list kafka:29092 --topic $2 && echo 'Produced 100 messages.'"
        shift; shift
        ;;

        --test-sub)
        docker-compose exec kafka kafka-console-consumer \
            --bootstrap-server "kafka:9092" \
            --topic "$2" \
            --from-beginning \
            --max-messages 100
        shift; shift
        ;;

        *)
        if [[ "$1" != "" ]]; then
            echo "ERROR! Invalid argument '$1'"
            exit 1
        fi
        ;;

    esac
done

exit 0
