import { Router } from "express";
import {
  getAdverseActionsController,
  createAdverseActionController,
} from "../controllers/AdverseActionController";
import { isAuth } from "../middleware/auth";
import { createAdverseActionSchema } from "../utils/validations";
import validate from "../middleware/validator";

const adverseActionRouter = Router();

adverseActionRouter.get("/", isAuth, getAdverseActionsController);
adverseActionRouter.post(
  "/",
  isAuth,
  validate(createAdverseActionSchema),
  createAdverseActionController
);

export default adverseActionRouter;
