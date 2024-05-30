package com.example.producer.config;

import com.example.producer.utility.Constants;
import org.apache.kafka.clients.admin.NewTopic;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.kafka.config.TopicBuilder;

import java.util.ArrayList;
import java.util.List;


@Configuration
public class KafkaConfig {

    @Value("${kafka.topics}")
    private String[] topics;


    @Bean
    public NewTopic topic() {
        return TopicBuilder
                .name(Constants.TOPIC_NAME)
                .partitions(2)
                .replicas(2)
                .build();
    }
}
