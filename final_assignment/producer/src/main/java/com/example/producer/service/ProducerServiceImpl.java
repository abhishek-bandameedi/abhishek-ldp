package com.example.producer.service;

import com.example.producer.dto.PostDto;
import com.example.producer.entity.Post;
import com.example.producer.repository.SocialMediaRepository;
import com.example.producer.utility.Constants;
import lombok.extern.slf4j.Slf4j;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
@Slf4j
public class ProducerServiceImpl implements ProducerService{
    private final KafkaTemplate<String, Object> kafkaTemplate;
    private final SocialMediaRepository socialMediaRepository;
    private final ModelMapper modelMapper;
    @Autowired
    public ProducerServiceImpl(KafkaTemplate<String,Object> kafkaTemplate, SocialMediaRepository socialMediaRepository, ModelMapper modelMapper){
        this.kafkaTemplate = kafkaTemplate;
        this.socialMediaRepository = socialMediaRepository;
        this.modelMapper = modelMapper;
    }

    @Transactional
    @Override
    public void postContent(PostDto postDto) {
        try {
            log.info("Posting data event to Kafka topic: {}", Constants.TOPIC_NAME);
            kafkaTemplate.send(Constants.TOPIC_NAME, postDto);
            log.info("Posting data event sent successfully to Kafka topic: {}", Constants.TOPIC_NAME);
            Post newPost = modelMapper.map(postDto, Post.class);
            socialMediaRepository.save(newPost);
            log.info("Post saved successfully");
        } catch (Exception e) {
            log.error("Error occurred while posting content: {}", e.getMessage());
        }
    }

    @Override
    public List<Post> getAllPosts() {
        return socialMediaRepository.findAll();
    }
}
