package br.avcaliani.spring.app.kafka

import br.avcaliani.spring.app.Constants.SALES_TOPIC
import br.avcaliani.spring.app.model.Sale
import org.slf4j.LoggerFactory
import org.springframework.kafka.annotation.KafkaListener
import org.springframework.stereotype.Service


@Service
class KafkaConsumer {

    private val logger = LoggerFactory.getLogger(KafkaConsumer::class.java)

    @KafkaListener(topics = [SALES_TOPIC])
    fun consume(sale: Sale?) =
        // Here you can do whatever you need \o/
        logger.info("New Sale -> $sale")
}