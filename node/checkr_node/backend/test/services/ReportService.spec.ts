import chai, { expect } from 'chai';
import sinon from 'sinon';
import chaiAsPromised from 'chai-as-promised';
import { Report } from '../../src/models/Report';
import { Candidate } from '../../src/models/Candidate';
import { ReportService } from '../../src/services/ReportService';
import CandidateNotFoundException from '../../src/exceptions/CandidateNotFoundException';
import { CreateReportSchemaType } from '../../src/utils/validations';

chai.use(chaiAsPromised);

describe('ReportService', () => {
  let findAllStub: sinon.SinonStub;
  let findByPkStub: sinon.SinonStub;
  let createStub: sinon.SinonStub;
  let saveStub: sinon.SinonStub;

  beforeEach(() => {
    findAllStub = sinon.stub(Report, 'findAll');
    findByPkStub = sinon.stub(Candidate, 'findByPk');
    createStub = sinon.stub(Report, 'create');
    saveStub = sinon.stub(Report.prototype, 'save');
  });

  afterEach(() => {
    sinon.restore();
  });

  describe('getAllReports', () => {
    it('should return all reports', async () => {
      const reports = [{ id: 1, status: 'clear' }];
      findAllStub.resolves(reports as Report[]);

      const result = await ReportService.getAllReports();
      expect(result).to.equal(reports);
    });
  });

  describe('getReportByCandidateId', () => {
    it('should return the report if found', async () => {
      const candidate = {
        id: 1,
        report: { id: 1, status: 'clear' }
      };
      findByPkStub.resolves(candidate as Candidate);

      const result = await ReportService.getReportByCandidateId(1);
      expect(result).to.equal(candidate.report);
    });

    it('should throw CandidateNotFoundException if candidate or report not found', async () => {
      findByPkStub.resolves(null);
      await expect(ReportService.getReportByCandidateId(1)).to.be.rejectedWith(CandidateNotFoundException, 'Candidate with id 1 not found');
    });
  });

  describe('updateAdjudication', () => {
    it('should update the adjudication status and return the report', async () => {
      const report = {
        id: 1,
        status: 'clear',
        adjudication: '-',
        save: saveStub
      };
      findByPkStub.resolves({ id: 1, report } as unknown as Candidate);
      saveStub.resolves(report);

      const result = await ReportService.updateAdjudication(1, 'engage');
      expect(result.adjudication).to.equal('engage');
    });
  });

  describe('createReport', () => {
    it('should create and return the new report', async () => {
      const reportData: CreateReportSchemaType = {
        status: 'clear',
        adjudication: '-',
        package: 'basic',
        created_At: '2024-05-22T14:20:00.000Z',
        completed_at: '2024-05-22T14:20:00.000Z',
        candidateId: 1
      };

      const report = { id: 1, ...reportData };
      createStub.resolves(report as unknown as Report);

      const result = await ReportService.createReport(reportData);
      expect(result).to.equal(report);
    });
  });
});
