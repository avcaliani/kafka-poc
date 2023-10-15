package br.avcaliani.spring.app.kafka

import br.avcaliani.spring.app.model.Sale
import org.apache.kafka.clients.consumer.ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG
import org.apache.kafka.clients.consumer.ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG
import org.apache.kafka.common.serialization.StringDeserializer
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.autoconfigure.kafka.KafkaProperties
import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import org.springframework.kafka.annotation.EnableKafka
import org.springframework.kafka.config.ConcurrentKafkaListenerContainerFactory
import org.springframework.kafka.core.DefaultKafkaConsumerFactory
import org.springframework.kafka.support.serializer.JsonDeserializer


@Configuration
@EnableKafka
class KafkaConfig {

    @Autowired
    private lateinit var kafkaProps: KafkaProperties

    /**
     * This method will return consumer properties.
     * The method "buildConsumerProperties()" retrieves all kafka configs you made in properties file.
     */
    @Bean
    fun consumerConfigs(): Map<String, Any?> {
        //
        val props: MutableMap<String, Any?> = HashMap(kafkaProps.buildConsumerProperties())
        props[KEY_DESERIALIZER_CLASS_CONFIG] = StringDeserializer::class.java
        props[VALUE_DESERIALIZER_CLASS_CONFIG] = JsonDeserializer::class.java
        return kafkaProps.buildConsumerProperties()
    }

    @Bean
    fun consumerFactory() = DefaultKafkaConsumerFactory(
        consumerConfigs(),
        StringDeserializer(),
        JsonDeserializer(Sale::class.java)
    )

    @Bean
    fun kafkaListenerContainerFactory(): ConcurrentKafkaListenerContainerFactory<String, Sale> {
        val factory = ConcurrentKafkaListenerContainerFactory<String, Sale>()
        factory.consumerFactory = consumerFactory()
        return factory
    }

}