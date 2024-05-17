import { Table, Column, Model, HasMany, DataType } from 'sequelize-typescript';
import Post from './Post';

@Table({
  tableName: 'users', 
})
export default class User extends Model<User> {
  @Column({
    allowNull: false,
    type: DataType.STRING,
  })
  name!: string;

  @HasMany(() => Post)
  posts!: Post[];
}