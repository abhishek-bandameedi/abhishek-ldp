package com.example.producer.service;

public interface ProducerService {
    public void placeOrder(String orderDetails);
    public void changeInventory(String inventoryUpdate);
    public void payment(String paymentDetails);
    public void smsNotifications(String smsNotification);
    public void deliveryUpdate(String deliveryStatus);
}