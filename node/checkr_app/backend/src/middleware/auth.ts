import jwt, { JwtPayload } from "jsonwebtoken";
import * as dotenv from "dotenv";
import { Request as ExpressRequest, Response, NextFunction } from "express";

dotenv.config();

const { JWT_SECRET } = process.env;

interface AuthRequest extends ExpressRequest {
  userId?: string;
}
interface TokenPayload extends JwtPayload {
  userId?: string;
}

export const isAuth = (req: AuthRequest, res: Response, next: NextFunction) => {
  const authHeader = req.get("Authorization");
  if (!authHeader) {
    return res.status(401).json({
      message: "Not authenticated",
    });
  }
  const token = authHeader.split(" ")[1];
  let decodedToken: TokenPayload;
  try {
    decodedToken = jwt.verify(token, JWT_SECRET as string) as TokenPayload;
  } catch (error) {
    return res.status(401).json({
      message: "Invalid token",
    });
  }
  if (!decodedToken) {
    return res.status(401).json({
      message: "Invalid token",
    });
  }

  req.userId = decodedToken.userId;
  next();
};
