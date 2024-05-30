import { Router } from "express";
import {
  createReportController,
  getAllReportsController,
  getReportByCandidateIdController,
  updateAdjudicationController,
} from "../controllers/ReportController";
import { isAuth } from "../middleware/auth";
import validate from "../middleware/validator";
import { createCandidateSchema } from "../utils/validations";

const reportRouter = Router();

reportRouter.get("/", isAuth, getAllReportsController);
reportRouter.get("/:candidateId", isAuth, getReportByCandidateIdController);
reportRouter.post(
  "/",
  isAuth,
  validate(createCandidateSchema),
  createReportController
);
reportRouter.put("/:candidateId", isAuth, updateAdjudicationController);

export default reportRouter;
