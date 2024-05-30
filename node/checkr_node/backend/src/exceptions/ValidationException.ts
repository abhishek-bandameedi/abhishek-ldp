import HttpException from './HttpException';

export default class ValidationException extends HttpException {
  public errors: any;

  constructor(errors: any) {
    super(422, 'Validation Error');
    this.errors = errors;
  }
}