import chai, { expect } from 'chai';
import sinon from 'sinon';
import chaiAsPromised from 'chai-as-promised';
import { Candidate } from '../../src/models/Candidate';
import { CandidateService } from '../../src/services/CandidateService';
import CandidateNotFoundException from '../../src/exceptions/CandidateNotFoundException';
import { CreateCandidateSchemaType } from '../../src/utils/validations';

chai.use(chaiAsPromised);

describe('CandidateService', () => {
  let findAllStub: sinon.SinonStub;
  let findByPkStub: sinon.SinonStub;
  let createStub: sinon.SinonStub;

  beforeEach(() => {
    findAllStub = sinon.stub(Candidate, 'findAll');
    findByPkStub = sinon.stub(Candidate, 'findByPk');
    createStub = sinon.stub(Candidate, 'create');
  });

  afterEach(() => {
    sinon.restore();
  });

  describe('getAllCandidates', () => {
    it('should return all candidates', async () => {
      const candidates = [{ id: 1, candidate_name: 'John Doe' }];
      findAllStub.resolves(candidates as Candidate[]);

      const result = await CandidateService.getAllCandidates();
      expect(result).to.equal(candidates);
    });
  });

  describe('getCandidateById', () => {
    it('should return the candidate if found', async () => {
      const candidate = { id: 1, candidate_name: 'John Doe' };
      findByPkStub.resolves(candidate as Candidate);

      const result = await CandidateService.getCandidateById(1);
      expect(result).to.equal(candidate);
    });

    it('should throw CandidateNotFoundException if candidate not found', async () => {
      findByPkStub.resolves(null);
      await expect(CandidateService.getCandidateById(1)).to.be.rejectedWith(CandidateNotFoundException, 'Candidate with id 1 not found');
    });
  });

  describe('createCandidate', () => {
    it('should create and return the new candidate', async () => {
      const candidateData: CreateCandidateSchemaType = {
        candidate_name: 'Jane Doe',
        candidate_email: 'jane.doe@example.com',
        dob: '1990-01-01',
        zipcode: '12345',
        phone_no: '1234567890',
        location: 'NYC',
        social_security_no: '123-45-6789',
        driver_liscence: 'A1234567',
        created_at: '2024-05-22T14:20:00.000Z',
        userId: 1,
      };

      const candidate = { id: 1, ...candidateData };
      createStub.resolves(candidate as unknown as Candidate);

      const result = await CandidateService.createCandidate(candidateData);
      expect(result).to.equal(candidate);
    });
  });
});
