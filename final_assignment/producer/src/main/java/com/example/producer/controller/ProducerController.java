package com.example.producer.controller;

import com.example.producer.dto.PostDto;
import com.example.producer.entity.Post;
import com.example.producer.service.ProducerService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Slf4j
@RestController
@RequestMapping("api/v1/kafka")
public class ProducerController {
    private final ProducerService producerService;

    @Autowired
    public ProducerController(ProducerService producerService) {
        this.producerService = producerService;
    }

    @PostMapping("/post-content")
    public String postContent(@RequestBody PostDto postDto){
        producerService.postContent(postDto);
        log.info("Content posted successfully");
        return "Content posted successfully";
    }
    @GetMapping("/posts")
    public List<Post> getPosts(){
        log.info("Fetching all posts");
        return producerService.getAllPosts();
    }
}
