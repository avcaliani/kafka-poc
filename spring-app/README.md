# 🍃 Spring Kafka
By Anthony Vilarim Caliani

![#](https://img.shields.io/badge/license-MIT-blue.svg) ![#](https://img.shields.io/badge/java-11-red.svg) ![#](https://img.shields.io/badge/spring--boot-2.4.5-green.svg)

## API
```sh
# Development
API_URL="http://localhost:8080"    # Docker
# API_URL="http://localhost:9000"  # Dev

# Actuator Endpoints
curl "$API_URL/actuator/health" | json_pp

curl "$API_URL/actuator/health/kafka" | json_pp

# Publish \o/
curl -X POST \
  -H "Content-Type: application/json" \
  --data '{ "user": "anthony", "product": { "name": "orange", "price": 0.99 }, "quantity": 16 }' \
  "$API_URL/v1/sale" | json_pp
```

Now, keep your eyes on application console because everything will be logged 😉

## Related Links
- [Spring Docs: Kafka Client Compatibility](https://spring.io/projects/spring-kafka)
- [Spring Docs: Apache Kafka](https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-messaging.html#boot-features-kafka)
