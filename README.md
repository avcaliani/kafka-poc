# ✉️ Kafka PoC

By Anthony Vilarim Caliani

![License](https://img.shields.io/github/license/avcaliani/kafka-poc?logo=apache&color=lightseagreen)
![#](https://img.shields.io/badge/python-3.x-yellow.svg)
![#](https://img.shields.io/badge/apache--spark-3.1.x-ff4757.svg)
![#](https://img.shields.io/badge/spring--boot-2.4.5-green.svg)

This is my Apache Kafka repository.  
Here you will find some stuff that I've done while I was learning about how to work with Apache Kafka.

In this repository you will find some experiments...

| project      | description                                        |
|--------------|----------------------------------------------------|
| `py-app`     | Simple Kafka producer and consumer in Python.      |
| `spark-app`  | PySpark Kafka consumer (streaming and batch).      |
| `spring-app` | Spring Boot API that produce and consume messages. |

## Quick Start

Before you start exploring the projects you have to "up" your own kafka.

```bash
# Create Kafka and Zookeper containers
docker-compose up -d

# Checking if everything is okay
docker-compose ps

# Checking Zookeper
docker-compose logs zookeeper | grep -i binding

# Checking Kafka (It may take a few seconds to start)
docker-compose logs kafka | grep -i started
```

### Let's test it?

```bash
# Create a new topic
./kafka.sh --create   "sales-topic"

# Checking if it worked
./kafka.sh --describe "sales-topic"

# Optional!
# The next steps are optional, you cant try them in case you want to test the kafka via CLI.

# Kafka Producer
./kafka.sh --test-pub "sales-topic"

# Kafka Consumer
./kafka.sh --test-sub "sales-topic"
```

### Related Links

- [Kafka Tool - UI Tool 4 Kafka](https://www.kafkatool.com/download.html)
- [Medium: Aprendendo na prática](https://medium.com/trainingcenter/apache-kafka-codifica%C3%A7%C3%A3o-na-pratica-9c6a4142a08f)
- [Github: Confluent Inc. (Apache Kafka®)](https://github.com/confluentinc/cp-docker-images)

---

🧙‍♂️ _"If in doubt Meriadoc, always follow your nose." - Gandalf_
