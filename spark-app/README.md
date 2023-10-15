#  Spark App
By Anthony Vilarim Caliani

![#](https://img.shields.io/badge/license-MIT-blue.svg) ![#](https://img.shields.io/badge/python-3.8.x-yellow.svg) ![#](https://img.shields.io/badge/spark-3.1.1-orange.svg)

## Quick Start
```sh
# Go to project "root" to use docker-compose :)
cd ..

# Starting Streaming Job
docker-compose exec spark-app /app/run.sh streaming

# Starting Batch Job
docker-compose exec spark-app /app/run.sh batch
```

Now, keep your eyes on application console because everything will be logged 😉

## Related Links
- [Structured Streaming - Guide](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html)
- [Structured Streaming - Kafka Guide](https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html)
