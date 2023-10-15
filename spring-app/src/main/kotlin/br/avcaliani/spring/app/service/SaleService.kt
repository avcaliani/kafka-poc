package br.avcaliani.spring.app.service

import br.avcaliani.spring.app.kafka.KafkaProducer
import br.avcaliani.spring.app.model.Sale
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.beans.factory.annotation.Value
import org.springframework.stereotype.Service
import java.time.Instant
import java.time.ZoneOffset
import java.time.format.DateTimeFormatter

@Service
class SaleService {

    @Value("\${app.source}")
    private lateinit var source: String

    @Autowired
    private lateinit var kafka: KafkaProducer

    fun save(sale: Sale): Sale {
        val newSale = prepare(sale)
        kafka.send(newSale)
        return newSale
    }

    private fun prepare(sale: Sale): Sale =
        sale.copy(
            total = (sale.product?.price?.times(sale.quantity ?: 0)),
            createdAt = now(),
            source = source
        )

    private fun now() =
        DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")
            .withZone(ZoneOffset.UTC)
            .format(Instant.now())
}