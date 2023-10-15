package br.avcaliani.spring.app.kafka

import org.apache.kafka.clients.admin.AdminClient
import org.apache.kafka.clients.admin.DescribeClusterOptions
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.actuate.health.Health
import org.springframework.boot.actuate.health.HealthIndicator
import org.springframework.kafka.core.KafkaAdmin
import org.springframework.stereotype.Component

@Component
class KafkaHealthIndicator : HealthIndicator {

    @Autowired
    private lateinit var kafkaAdmin: KafkaAdmin

    override fun health(): Health {
        val options = DescribeClusterOptions().timeoutMs(1000)
        val props = kafkaAdmin.configurationProperties
        return try {
            // When Kafka is not connected, describeCluster() method throws
            // an exception which in turn sets this indicator as being DOWN.
            AdminClient
                .create(props)
                .describeCluster(options)
            Health.up()
                .withDetail("properties", props).build()
        } catch (ex: Exception) {
            Health.down().withException(ex).build()
        }
    }

}