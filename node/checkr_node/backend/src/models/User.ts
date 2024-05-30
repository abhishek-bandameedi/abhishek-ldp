import { Table, Column, Model, HasMany } from 'sequelize-typescript';
import { Candidate } from './Candidate';

@Table
export class User extends Model {
  @Column
  email!: string;

  @Column
  password!: string;

  @HasMany(() => Candidate)
  candidates!: Candidate[];
}
