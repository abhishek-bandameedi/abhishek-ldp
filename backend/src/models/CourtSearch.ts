import { Table, Column, Model, DataType, ForeignKey, BelongsTo } from 'sequelize-typescript';
import { Candidate } from './Candidate';

@Table
export class CourtSearch extends Model {
  @Column
  search!: string;

  @Column
  status!: string;

  @Column({
    type: DataType.DATE
  })
  date!: Date;

  @ForeignKey(() => Candidate)
  @Column
  candidateId!: number;

  @BelongsTo(() => Candidate)
  candidate!: Candidate;
}
