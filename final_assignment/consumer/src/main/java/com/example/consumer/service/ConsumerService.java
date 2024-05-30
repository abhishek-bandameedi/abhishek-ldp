package com.example.consumer.service;

import com.example.consumer.dto.PostDto;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
public class ConsumerService {
    @KafkaListener(topics = "posts",groupId = "group_id-1")
    public void consumePosts(ConsumerRecord<String, PostDto> post){
        System.out.println("Post recieved: "+post.value());
    }
}
