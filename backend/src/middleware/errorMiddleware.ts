import { Request, Response, NextFunction } from 'express';
import HttpException from '../exceptions/HttpException';

import ValidationException from '../exceptions/ValidationException';

function errorMiddleware(error: HttpException, req: Request, res: Response, next: NextFunction) {
  const status = error.status || 500;
  const message = error.message || 'Something went wrong';
  
  if (error instanceof ValidationException) {
    res.status(status).send({
      status,
      message,
      errors: error.errors, 
    });
  } else {
    res.status(status).send({
      status,
      message,
    });
  }
}

export default errorMiddleware;