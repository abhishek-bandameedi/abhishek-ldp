import { Table, Column, Model, ForeignKey, BelongsTo, DataType } from 'sequelize-typescript';
import User from './User';

@Table({
  tableName: 'posts', 
})
export default class Post extends Model<Post> {
  @Column({
    allowNull: false,
    type: DataType.STRING,
  })
  title!: string;

  @Column({
    allowNull: false,
    type: DataType.TEXT,
  })
  content!: string;

  @ForeignKey(() => User)
  @Column({
    allowNull: false,
  })
  userId!: number;

  @BelongsTo(() => User)
  user!: User;
}