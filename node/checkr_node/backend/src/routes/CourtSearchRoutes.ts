import { Router } from "express";
import {
  createCourtSearchController,
  getCourtSearchByCandidateIdController,
} from "../controllers/CourtSearchController";
import { isAuth } from "../middleware/auth";
import validate from "../middleware/validator";
import { createCourtSearchSchema } from "../utils/validations";

const courtSearchRouter = Router();

courtSearchRouter.get(
  "/:candidateId",
  isAuth,
  getCourtSearchByCandidateIdController
);
courtSearchRouter.post(
  "/",
  isAuth,
  validate(createCourtSearchSchema),
  createCourtSearchController
);

export default courtSearchRouter;
