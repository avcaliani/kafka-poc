package br.avcaliani.spring.app.kafka

import br.avcaliani.spring.app.Constants.SALES_TOPIC
import br.avcaliani.spring.app.model.Sale
import org.slf4j.LoggerFactory
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.kafka.core.KafkaTemplate
import org.springframework.stereotype.Service


@Service
class KafkaProducer {

    private val logger = LoggerFactory.getLogger(KafkaConsumer::class.java)

    @Autowired
    private lateinit var kafka: KafkaTemplate<String, Sale>

    fun send(data: Sale) {
        logger.info("Message Sent! data='{}' | topic='{}'", data, SALES_TOPIC)
        kafka.send(SALES_TOPIC, data)
    }

}