package com.example.producer.config;
import org.apache.kafka.clients.admin.NewTopic;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import java.util.ArrayList;
import java.util.List;


@Configuration
public class KafkaConfig {

    @Value("${kafka.topics}")
    private String[] topics;


    @Bean
    public List<NewTopic> kafkaTopics() {
        List<NewTopic> newTopics = new ArrayList<>();
        for (String topicName : topics) {
            newTopics.add(new NewTopic(topicName, 10, (short) 2));
        }
        return newTopics;
    }
}

