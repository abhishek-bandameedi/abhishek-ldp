import { Request, Response, NextFunction } from "express";
import { CourtSearchService } from "../services/CourtSearchService";
import CandidateNotFoundException from "../exceptions/CandidateNotFoundException";
import { CreateCourtSearchSchemaType, createCourtSearchSchema } from "../utils/validations";
import ValidationException from "../exceptions/ValidationException";

export const getCourtSearchByCandidateIdController = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const candidateId = parseInt(req.params.candidateId, 10);
    if (isNaN(candidateId)) {
      return res.status(400).json({ error: "Invalid candidate ID" });
    }

    const courtSearch = await CourtSearchService.getCourtSearchByCandidateId(
      candidateId
    );
    res.status(200).json(courtSearch);
  } catch (error) {
    if (error instanceof CandidateNotFoundException) {
      return res.status(404).json({ error: error.message });
    }
    next(error);
  }
};

export const createCourtSearchController = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const courtSearchData: CreateCourtSearchSchemaType = req.body;
    const validationResult = createCourtSearchSchema.safeParse(courtSearchData);
    if (!validationResult.success) {
      throw new ValidationException(validationResult.error.errors);
    }

    const courtSearches = await CourtSearchService.createCourtSearch(
      courtSearchData
    );
    res.status(201).json(courtSearches);
  } catch (error) {
    next(error);
  }
};
