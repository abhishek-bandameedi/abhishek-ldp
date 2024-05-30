import { Request, Response, NextFunction } from 'express';
import { CandidateService } from '../services/CandidateService'; 
import CandidateNotFoundException from '../exceptions/CandidateNotFoundException';
import { CreateCandidateSchemaType, createCandidateSchema } from '../utils/validations';
import ValidationException from '../exceptions/ValidationException';

export const getAllCandidatesController = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const candidates = await CandidateService.getAllCandidates();
    res.status(200).json(candidates);
  } catch (error) {
    next(error);
  }
};

export const getCandidateByIdController = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const candidateId = parseInt(req.params.id, 10);
    const candidate = await CandidateService.getCandidateById(candidateId);
    if (!candidate) {
      throw new CandidateNotFoundException(candidateId);
    }
    res.status(200).json(candidate);
  } catch (error) {
    next(error);
  }
};

export const createCandidateController = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const candidateData: CreateCandidateSchemaType = req.body;
    const validationResult = createCandidateSchema.safeParse(candidateData);
    if (!validationResult.success) {
      throw new ValidationException(validationResult.error.errors);
    }

    const newCandidate = await CandidateService.createCandidate(candidateData);
    res.status(201).json(newCandidate);
  } catch (error) {
    next(error);
  }
};
