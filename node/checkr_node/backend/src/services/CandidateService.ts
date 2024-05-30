import { Candidate } from "../models/Candidate";
import CandidateNotFoundException from "../exceptions/CandidateNotFoundException";
import { CreateCandidateSchemaType } from "../utils/validations";

const getAllCandidates = async (): Promise<Candidate[]> => {
  return Candidate.findAll();
};

const getCandidateById = async (
  candidateId: number
): Promise<Candidate | null> => {
  const candidate = await Candidate.findByPk(candidateId);
  if (!candidate) {
    throw new CandidateNotFoundException(candidateId);
  }
  return candidate;
};

const createCandidate = async (
  candidateData: CreateCandidateSchemaType
): Promise<Candidate> => {
  return await Candidate.create(candidateData);
};

export const CandidateService = {
  getAllCandidates,
  getCandidateById,
  createCandidate,
};
