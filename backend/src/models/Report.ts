import { Table, Column, Model, DataType, ForeignKey, BelongsTo } from 'sequelize-typescript';
import { Candidate } from './Candidate';

@Table
export class Report extends Model {
  @Column({
    type: DataType.ENUM,
    values: ['clear', 'consider', 'schedule']
  })
  status!: 'clear' | 'consider' | 'schedule';

  @Column({
    type: DataType.ENUM,
    values: ['-', 'adverse-action', 'engage']
  })
  adjudication!: '-' | 'adverse-action' | 'engage';

  @Column
  package!: string;

  @Column({
    type: DataType.DATE
  })
  created_At!: Date;

  @Column({
    type: DataType.DATE
  })
  completed_at!: Date;

  @ForeignKey(() => Candidate)
  @Column
  candidateId!: number;

  @BelongsTo(() => Candidate)
  candidate!: Candidate;
}
