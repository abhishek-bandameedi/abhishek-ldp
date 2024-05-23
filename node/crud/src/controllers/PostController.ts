import { Request, Response, NextFunction } from "express";
import Post from "../models/Post";
import PostNotFoundException from "../exceptions/PostNotFoundException";

export const createPost = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const post = await Post.create(req.body);
    res.status(201).json(post);
  } catch (error) {
    next(error);
  }
};

export const getPosts = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const page = parseInt(req.query.page as string,10) || 1;
    const size = parseInt(req.query.size as string,10) || 10;

    const offset = (page - 1) * size;
    const limit = size;

    const {count, rows:posts} = await Post.findAndCountAll({
        offset,
        limit,
        include:['user'],
    })
    res.status(200).json({
        totalItems: count,
        totalPages: Math.ceil(count/size),
        currentPage: page,
        posts,
    });
  } catch (error) {
    next(error);
  }
};

export const getPostById = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const post = await Post.findByPk(req.params.id, { include: ["user"] });
    if (!post) {
      throw new PostNotFoundException(req.params.id);
    }
    res.status(200).json(post);
  } catch (error) {
    next(error);
  }
};

export const updatePost = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const post = await Post.findByPk(req.params.id);
    if (!post) {
      throw new PostNotFoundException(req.params.id);
    }
    post.title = req.body.title;
    post.content = req.body.content;
    await post.save();
    res.status(200).json(post);
  } catch (error) {
    next(error);
  }
};

export const deletePost = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const post = await Post.findByPk(req.params.id);
    if (!post) {
      throw new PostNotFoundException(req.params.id);
    }
    await post.destroy();
    res.status(200).json({ message: "Post deleted successfully" });
  } catch (error) {
    next(error);
  }
};
