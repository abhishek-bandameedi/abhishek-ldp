package com.example.producer.controller;

import com.example.producer.service.ProducerService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@Slf4j
@RestController
@RequestMapping("/api/v1/kafka")
public class ProducerController {

    private final ProducerService producerService;

    @Autowired
    public ProducerController(ProducerService producerService) {
        this.producerService = producerService;
    }

    @PostMapping("/place-order")
    public ResponseEntity<?> placeOrder(@RequestParam String orderDetails) {
        producerService.placeOrder(orderDetails);
        log.info("Order placed successfully: {}", orderDetails);
        return ResponseEntity.ok("Order message sent successfully");
    }

    @PostMapping("/update-inventory")
    public ResponseEntity<?> updateInventory(@RequestParam String inventoryUpdate) {
        producerService.changeInventory(inventoryUpdate);
        log.info("Inventory update message sent: {}", inventoryUpdate);
        return ResponseEntity.ok("Inventory update message sent successfully");
    }

    @PostMapping("/process-payment")
    public ResponseEntity<?> processPayment(@RequestParam String paymentDetails) {
        producerService.payment(paymentDetails);
        log.info("Payment processed successfully: {}", paymentDetails);
        return ResponseEntity.ok("Payment transaction message sent successfully");
    }

    @PostMapping("/send-customer-notification")
    public ResponseEntity<?> sendCustomerNotification(@RequestParam String smsNotification) {
        producerService.smsNotifications(smsNotification);
        log.info("Customer notification sent successfully: {}", smsNotification);
        return ResponseEntity.ok("Customer notification message sent successfully");
    }

    @PostMapping("/update-shipping")
    public ResponseEntity<?> updateShipping(@RequestParam String deliveryStatus) {
        producerService.deliveryUpdate(deliveryStatus);
        log.info("Shipping update message sent successfully: {}", deliveryStatus);
        return ResponseEntity.ok("Shipping update message sent successfully");
    }
}