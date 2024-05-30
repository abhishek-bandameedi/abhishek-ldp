import { Request, Response, NextFunction } from 'express';
import { ReportService } from '../services/ReportService';
import CandidateNotFoundException from '../exceptions/CandidateNotFoundException';
import { CreateReportSchemaType, createReportSchema } from '../utils/validations';
import ValidationException from '../exceptions/ValidationException';

export const getAllReportsController = async (req: Request, res: Response, next: NextFunction) => {
  try {
    const reports = await ReportService.getAllReports();
    res.status(200).json(reports);
  } catch (error) {
    next(error);
  }
};

export const getReportByCandidateIdController = async (req: Request, res: Response, next: NextFunction) => {
  try {
    const candidateId = parseInt(req.params.candidateId, 10);
    const report = await ReportService.getReportByCandidateId(candidateId);
    res.status(200).json(report);
  } catch (error) {
    if (error instanceof CandidateNotFoundException) {
      res.status(404).json({ message: error.message });
    } else {
      next(error);
    }
  }
};

export const updateAdjudicationController = async (req: Request, res: Response, next: NextFunction) => {
  try {
    const candidateId = parseInt(req.params.candidateId, 10);
    const { adjudication } = req.body;
    if (!['-', 'adverse-action', 'engage'].includes(adjudication)) {
      return res.status(400).json({ message: 'Invalid adjudication value' });
    }
    const updatedReport = await ReportService.updateAdjudication(candidateId, adjudication);
    res.status(200).json(updatedReport);
  } catch (error) {
    if (error instanceof CandidateNotFoundException) {
      res.status(404).json({ message: error.message });
    } else {
      next(error);
    }
  }
};

export const createReportController = async (req: Request, res: Response, next: NextFunction) => {
  try {
    const reportData: CreateReportSchemaType = req.body;

    const validationResult = createReportSchema.safeParse(reportData);
    if (!validationResult.success) {
      throw new ValidationException(validationResult.error.errors);
    }

    const newReport = await ReportService.createReport(reportData);
    res.status(201).json(newReport);
  } catch (error) {
    next(error);
  }
};