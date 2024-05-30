import { AdverseAction } from "../models/AdverseAction";
import { CreateAdverseActionSchemaType } from "../utils/validations";

const getAllAdverseActions = async (
  page: number = 1,
  size: number = 10
): Promise<{
  totalItems: number;
  totalPages: number;
  currentPage: number;
  adverseActions: AdverseAction[];
}> => {
  const offset = (page - 1) * size;
  const limit = size;

  const {count, rows:adverseActions} = await AdverseAction.findAndCountAll({
    offset,
    limit,
  });
  return {
    totalItems: count,
    totalPages: Math.ceil(count / size),
    currentPage: page,
    adverseActions,
  }
};

const createAdverseAction = async (adverseActionData: CreateAdverseActionSchemaType):Promise<AdverseAction> => {
    return AdverseAction.create(adverseActionData);
}

export const AdverseActionService = {
    getAllAdverseActions,
    createAdverseAction
}