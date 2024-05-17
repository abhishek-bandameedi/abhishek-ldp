import Post from './models/Post';
import User from './models/User';
import { Sequelize } from 'sequelize-typescript';

const sequelize = new Sequelize({
  database: 'node',
  dialect: 'mysql',
  username: 'student',
  password: 'student',
  storage: ':memory:',
  models: [User,Post]
});

export default sequelize;