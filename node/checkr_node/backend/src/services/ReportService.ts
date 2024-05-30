import { Report } from "../models/Report";
import { Candidate } from "../models/Candidate";
import CandidateNotFoundException from "../exceptions/CandidateNotFoundException";
import { CreateReportSchemaType } from "../utils/validations";

const getAllReports = async (): Promise<Report[]> => {
  return Report.findAll();
};

const getReportByCandidateId = async (candidateId: number): Promise<Report> => {
  const candidate = await Candidate.findByPk(candidateId, {
    include: [Report],
  });
  if (!candidate?.report) {
    throw new CandidateNotFoundException(candidateId);
  }
  return candidate.report;
};

const updateAdjudication = async (
  candidateId: number,
  adjudication: "-" | "adverse-action" | "engage"
): Promise<Report> => {
  const report = await getReportByCandidateId(candidateId);
  report.adjudication = adjudication;
  await report.save();
  return report;
};

const createReport = async (reportData: CreateReportSchemaType): Promise<Report> => {
  return await Report.create(reportData);
};

export const ReportService = {
  getReportByCandidateId,
  updateAdjudication,
  getAllReports,
  createReport
};
