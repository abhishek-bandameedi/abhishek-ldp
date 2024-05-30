package com.example.producer.service;

import com.example.producer.dto.PostDto;
import com.example.producer.entity.Post;

import java.util.List;

public interface ProducerService {
    public void postContent(PostDto postDto);
    public List<Post> getAllPosts();
}
