import { Request, Response, NextFunction } from "express";
import User from "../models/User";

export const createUser = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const user = await User.create(req.body);
    res.status(201).json(user);
  } catch (error) {
    next(error);
  }
};

export const getUsers = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const page = parseInt(req.query.page as string, 10) || 1;
    const size = parseInt(req.query.size as string, 10) || 10;

    const offset = (page - 1) * size;
    const limit = size;

    const { count, rows: users } = await User.findAndCountAll({
      offset,
      limit,
    });

    res.status(200).json({
      totalItems: count,
      totalPages: Math.ceil(count / size),
      currentPage: page,
      users,
    });
  } catch (error) {
    next(error);
  }
};
