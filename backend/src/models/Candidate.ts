import { Table, Column, Model, DataType, ForeignKey, BelongsTo, HasOne, HasMany } from 'sequelize-typescript';
import { User } from './User';
import { Report } from './Report';
import { CourtSearch } from './CourtSearch';
import { AdverseAction } from './AdverseAction';

@Table
export class Candidate extends Model {
  @Column
  candidate_name!: string;

  @Column
  zipcode!: string;

  @Column
  candidate_email!: string;

  @Column({
    type: DataType.DATEONLY,
  })
  dob!: Date;

  @Column
  phone_no!: string;

  @Column
  location!: string;

  @Column
  social_security_no!: string;

  @Column
  driver_liscence!: string;

  @Column({
    type: DataType.DATE,
  })
  created_at!: Date;

  @ForeignKey(() => User)
  @Column
  userId!: number;

  @BelongsTo(() => User)
  user!: User;

  @HasOne(() => Report)
  report!: Report;

  @HasOne(() => CourtSearch)
  courtSearch!: CourtSearch;

  @HasMany(() => AdverseAction)
  adverseActions!: AdverseAction[];
}
