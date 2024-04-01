package com.example.producer.repository;

import com.example.producer.entity.Post;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface SocialMediaRepository extends MongoRepository<Post,String> {
}
