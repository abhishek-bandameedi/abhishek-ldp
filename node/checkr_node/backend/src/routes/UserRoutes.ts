import { Router } from "express";
import {
  loginUserController,
  signUpUserController,
} from "../controllers/UserController";
import validate from "../middleware/validator";
import { loginSchema, signUpSchema } from "../utils/validations";

const userRouter = Router();

userRouter.post("/signup", validate(signUpSchema), signUpUserController);
userRouter.post("/login", validate(loginSchema), loginUserController);

export default userRouter;
