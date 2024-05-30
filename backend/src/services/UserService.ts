import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";
import * as dotenv from "dotenv";
import { User } from "../models/User";
import InvalidCredentialsException from "../exceptions/InvalidCredentialException";
import { loginSchemaType, signUpSchemaType } from "../utils/validations";

dotenv.config();

const { JWT_SECRET } = process.env;

export const signUpUser = async (data: signUpSchemaType) => {
  const { email, password } = data;
  const hashedPassword = await bcrypt.hash(password, 12);
  const user = await User.create({ email, password: hashedPassword });
  return user;
};

export const loginUser = async (data: loginSchemaType) => {
  const { email, password } = data;
  const user = await User.findOne({ where: { email } });
  if (!user) {
    throw new InvalidCredentialsException();
  }
  
  const passwordMatch = await bcrypt.compare(password, user.password);
  if (!passwordMatch) {
    throw new InvalidCredentialsException();
  }
  
  const token = jwt.sign(
    {
      email: user.email,
      userId: user.id.toString(),
    },
    JWT_SECRET as string,
    { expiresIn: "1h" }
  );

  return { user, token };
};
