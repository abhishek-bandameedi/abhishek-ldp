import { CourtSearch } from "../models/CourtSearch";
import CandidateNotFoundException from "../exceptions/CandidateNotFoundException";
import { Candidate } from "../models/Candidate";
import { CreateCourtSearchSchemaType } from "../utils/validations";

const getCourtSearchByCandidateId = async (
  candidateId: number
): Promise<CourtSearch | null> => {
  const candidate = await Candidate.findByPk(candidateId, {
    include: [CourtSearch],
  });
  if (!candidate?.courtSearch) {
    throw new CandidateNotFoundException(candidateId);
  }
  return candidate.courtSearch;
};

const createCourtSearch = (
  courtSearchData: CreateCourtSearchSchemaType
): Promise<CourtSearch> => {
  return CourtSearch.create(courtSearchData);
};

export const CourtSearchService = {
  getCourtSearchByCandidateId,
  createCourtSearch,
};
