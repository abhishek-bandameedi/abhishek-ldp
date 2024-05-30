import { Sequelize } from 'sequelize-typescript';
import { config } from 'dotenv';
import { User } from '../models/User';
import { Candidate } from '../models/Candidate';
import { Report } from '../models/Report';
import { CourtSearch } from '../models/CourtSearch';
import { AdverseAction } from '../models/AdverseAction';

config();

const sequelize = new Sequelize({
  dialect: 'mysql',
  host: process.env.DB_HOST,
  username: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  models: [User, Candidate, Report, CourtSearch, AdverseAction],
});

export { sequelize };
