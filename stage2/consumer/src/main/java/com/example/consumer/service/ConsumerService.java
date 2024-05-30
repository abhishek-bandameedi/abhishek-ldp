package com.example.consumer.service;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
public class ConsumerService {

    @KafkaListener(topics = "order_new_topic", groupId = "consumer-group1")
    public void consumeOrderUpdates(ConsumerRecord<String, String> record) {
        System.out.println("Consumed message from 'order_updates' topic: " + record.value());
    }

    @KafkaListener(topics = "inventory_topic", groupId = "consumer-group2")
    public void consumeInventoryChanges(ConsumerRecord<String, String> record) {
        System.out.println("Consumed message from 'inventory_changes' topic: " + record.value());
    }

    @KafkaListener(topics = "payment_topic", groupId = "consumer-group3")
    public void consumePaymentTransactions(ConsumerRecord<String, String> record) {
        System.out.println("Consumed message from 'payment_transactions' topic: " + record.value());
    }

    @KafkaListener(topics = "sms_notification_topic", groupId = "consumer-group4")
    public void consumeCustomerNotifications(ConsumerRecord<String, String> record) {
        System.out.println("Consumed message from 'customer_notifications' topic: " + record.value());
    }

    @KafkaListener(topics = "delivery_topic", groupId = "consumer-group5")
    public void consumeShippingUpdates(ConsumerRecord<String, String> record) {
        System.out.println("Consumed message from 'shipping_updates' topic: " + record.value());
    }
}