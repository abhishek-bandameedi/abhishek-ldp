package com.deliveryboy.service;

import com.deliveryboy.config.Constants;
import org.slf4j.LoggerFactory;
import org.slf4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;


@Service
public class KafkaService {
    @Autowired
    private KafkaTemplate<String,String> kafkaTemplate;
    private Logger logger = (Logger) LoggerFactory.getLogger(KafkaService.class);
    public boolean updateLocation(String loc){
        this.kafkaTemplate.send(Constants.LOCATION_TOPIC_NAME,loc);
        this.logger.info("message produced");
        return true;
    }
}
