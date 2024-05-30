import HttpException from './HttpException';

export default class CandidateNotFoundException extends HttpException {
  constructor(id: number) {
    super(404, `Candidate with id ${id} not found`);
  }
}