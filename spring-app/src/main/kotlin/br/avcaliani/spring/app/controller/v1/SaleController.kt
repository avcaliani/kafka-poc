package br.avcaliani.spring.app.controller.v1

import br.avcaliani.spring.app.Constants.V1
import br.avcaliani.spring.app.model.Sale
import br.avcaliani.spring.app.service.SaleService
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController

@RestController
@RequestMapping("$V1/sale")
class SaleController {

    @Autowired
    private lateinit var service: SaleService

    @PostMapping
    fun post(@RequestBody sale: Sale) = service.save(sale)

}