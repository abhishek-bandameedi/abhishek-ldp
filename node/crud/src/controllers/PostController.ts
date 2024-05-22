import { Request, Response } from 'express';
import Post from '../models/Post';

export const createPost = async (req: Request, res: Response) => {
  try {
    const post = await Post.create(req.body);
    return res.status(201).json(post);
  } catch (error) {
    return res.status(500).json({ error: 'Internal Server Error' });
  }
};

export const getPosts = async (req: Request, res: Response) => {
  try {
    const posts = await Post.findAll();
    return res.status(200).json(posts);
  } catch (error) {
    return res.status(500).json({ error: 'Internal Server Error' });
  }
};

export const getPostById = async (req: Request, res: Response) => {
  const { id } = req.params;
  try {
    const post = await Post.findByPk(id);
    if (!post) {
      return res.status(404).json({ error: 'Post not found' });
    }
    return res.status(200).json(post);
  } catch (error) {
    return res.status(500).json({ error: 'Internal Server Error' });
  }
};

export const updatePost = async (req: Request, res: Response) => {
  const { id } = req.params;
  try {
    const [updated] = await Post.update(req.body, {
      where: { id: id }
    });
    if (updated) {
      const updatedPost = await Post.findByPk(id);
      return res.status(200).json(updatedPost);
    }
    throw new Error('Post not found');
  } catch (error) {
    return res.status(500).json({ error: 'Internal Server Error' });
  }
};

export const deletePost = async (req: Request, res: Response) => {
  const { id } = req.params;
  try {
    const deleted = await Post.destroy({
      where: { id: id }
    });
    if (deleted) {
      return res.status(204).send('Post deleted');
    }
    throw new Error('Post not found');
  } catch (error) {
    return res.status(500).json({ error: 'Internal Server Error' });
  }
};