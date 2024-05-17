import { Router } from 'express';
import { createUser, getUsers } from '../controllers/UserController';
import { createPost, getPosts, getPostById, updatePost, deletePost } from '../controllers/PostController';

const router = Router();

router.post('/users', createUser);
router.get('/users', getUsers);

router.post('/posts', createPost);
router.get('/posts', getPosts);
router.get('/posts/:id', getPostById);
router.put('/posts/:id', updatePost);
router.delete('/posts/:id', deletePost);

export default router;