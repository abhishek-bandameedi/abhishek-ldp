import { Request, Response, NextFunction } from 'express';
import { AdverseActionService } from '../services/AdverseActionService'; // Adjust the import based on your project structure
import { CreateAdverseActionSchemaType, createAdverseActionSchema } from '../utils/validations';
import ValidationException from '../exceptions/ValidationException';

export const getAdverseActionsController = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const page = parseInt(req.query.page as string, 10) || 1;
    const size = parseInt(req.query.size as string, 10) || 10;

    const result = await AdverseActionService.getAllAdverseActions(page, size);

    res.status(200).json(result);
  } catch (error) {
    next(error);
  }
};

export const createAdverseActionController = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const adverseActionData: CreateAdverseActionSchemaType = req.body;

    const validationResult = createAdverseActionSchema.safeParse(adverseActionData);
    if (!validationResult.success) {
      throw new ValidationException(validationResult.error.errors);
    }

    const newAdverseAction = await AdverseActionService.createAdverseAction(adverseActionData);

    res.status(201).json(newAdverseAction);
  } catch (error) {
    next(error);
  }
};
