package com.example.producer.service.impl;
import com.example.producer.service.ProducerService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

@Service
@Slf4j
public class ProducerServiceImpl implements ProducerService {
    private final KafkaTemplate<String, Object> kafkaTemplate;

    @Autowired
    public ProducerServiceImpl(KafkaTemplate<String, Object> kafkaTemplate) {
        this.kafkaTemplate = kafkaTemplate;
    }

    @Override
    public void placeOrder(String orderDetails) {
        try {
            log.info("Placing order: {}", orderDetails);
            kafkaTemplate.send("order_new_topic", orderDetails);
        } catch (Exception e) {
            log.error("Error processing order: {}", e.getMessage(), e);
        }
    }

    @Override
    public void changeInventory(String inventoryUpdate) {
        try {
            log.info("Changing inventory: {}", inventoryUpdate);
            kafkaTemplate.send("inventory_topic", inventoryUpdate);
        } catch (Exception e) {
            log.error("Error processing inventory change: {}", e.getMessage(), e);
        }
    }

    @Override
    public void payment(String paymentDetails) {
        try {
            log.info("Processing payment: {}", paymentDetails);
            kafkaTemplate.send("payment_topic", paymentDetails);
        } catch (Exception e) {
            log.error("Error processing payment: {}", e.getMessage(), e);
        }
    }

    @Override
    public void smsNotifications(String smsNotification) {
        try {
            log.info("Sending SMS notification: {}", smsNotification);
            kafkaTemplate.send("sms_notification_topic", smsNotification);
        } catch (Exception e) {
            log.error("Error sending SMS notification: {}", e.getMessage(), e);
        }
    }

    @Override
    public void deliveryUpdate(String deliveryStatus) {
        try {
            log.info("Updating delivery status: {}", deliveryStatus);
            kafkaTemplate.send("delivery_topic", deliveryStatus);
        } catch (Exception e) {
            log.error("Error updating delivery status: {}", e.getMessage(), e);
        }
    }
}