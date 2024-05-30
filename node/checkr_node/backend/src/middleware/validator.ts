import { Request, Response, NextFunction } from "express";
import { ZodSchema, ZodError } from "zod";
import ValidationException from "../exceptions/ValidationException";

const validate = (schema: ZodSchema<any>) => (req: Request, res: Response, next: NextFunction) => {
  try {
    schema.parse(req.body);
    next();
  } catch (error) {
    if (error instanceof ZodError) {
      next(new ValidationException(error.errors));
    } else {
      next(error);
    }
  }
};

export default validate;