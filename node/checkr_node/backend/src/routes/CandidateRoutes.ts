import { Router } from "express";
import {
  getAllCandidatesController,
  getCandidateByIdController,
  createCandidateController,
} from "../controllers/CandidateController";
import { isAuth } from "../middleware/auth";
import validate from "../middleware/validator";
import { createCandidateSchema } from "../utils/validations";

const candidateRouter = Router();

candidateRouter.get("/", isAuth, getAllCandidatesController);
candidateRouter.get("/:id", isAuth, getCandidateByIdController);
candidateRouter.post(
  "/",
  isAuth,
  validate(createCandidateSchema),
  createCandidateController
);

export default candidateRouter;
