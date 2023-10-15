package br.avcaliani.spring.app.model

import com.fasterxml.jackson.annotation.JsonProperty

data class Sale(
    val user: String?,
    val product: Product?,
    val quantity: Int?,
    val total: Double?,
    @JsonProperty("created_at")
    val createdAt: String?,
    val source: String?
)
