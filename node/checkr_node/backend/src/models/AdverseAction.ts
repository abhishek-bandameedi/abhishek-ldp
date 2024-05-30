import { Table, Column, Model, DataType, ForeignKey, BelongsTo } from 'sequelize-typescript';
import { Candidate } from './Candidate';

@Table
export class AdverseAction extends Model {
  @Column
  status!: string;

  @Column({
    type: DataType.DATE
  })
  pre_notice_date!: Date;

  @Column({
    type: DataType.DATE
  })
  post_notice_date!: Date;

  @ForeignKey(() => Candidate)
  @Column
  candidateId!: number;

  @BelongsTo(() => Candidate)
  candidate!: Candidate;
}
