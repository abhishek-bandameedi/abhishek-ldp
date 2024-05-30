import { Request, Response, NextFunction } from "express";
import HttpException from "../exceptions/HttpException";
import { loginUser, signUpUser } from "../services/UserService";
import { loginSchemaType, signUpSchemaType } from "../utils/validations";
import { validationResult } from "express-validator";
import ValidationException from "../exceptions/ValidationException";

const isHttpException = (err: unknown): err is HttpException => {
  return (err as HttpException).status !== undefined;
};

export const signUpUserController = async (req: Request, res: Response, next: NextFunction) => {
  try {
    const data: signUpSchemaType = req.body;
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      throw new ValidationException(errors.array());
    }
    const user = await signUpUser(data);
    res.status(200).json(user);
  } catch (err) {
    if (isHttpException(err)) {
      next(err);
    } else {
      next(new HttpException(500, "Internal server error"));
    }
  }
};

export const loginUserController = async (req: Request, res: Response, next: NextFunction) => {
  try {
    const data: loginSchemaType = req.body;
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      throw new ValidationException(errors.array());
    }
    const { user, token } = await loginUser(data);

    res.status(200).json({
      message: "User logged in successfully",
      user_id: user.id.toString(),
      token: token,
    });
  } catch (err) {
    if (isHttpException(err)) {
      next(err);
    } else {
      next(new HttpException(500, "Internal server error"));
    }
  }
};
