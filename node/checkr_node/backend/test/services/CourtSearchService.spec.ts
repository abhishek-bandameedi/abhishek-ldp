import chai, { expect } from 'chai';
import sinon from 'sinon';
import chaiAsPromised from 'chai-as-promised';
import { CourtSearch } from '../../src/models/CourtSearch';
import { Candidate } from '../../src/models/Candidate';
import { CourtSearchService } from '../../src/services/CourtSearchService';
import CandidateNotFoundException from '../../src/exceptions/CandidateNotFoundException';
import { CreateCourtSearchSchemaType } from '../../src/utils/validations';

chai.use(chaiAsPromised);

describe('CourtSearchService', () => {
  let findByPkStub: sinon.SinonStub;
  let createStub: sinon.SinonStub;

  beforeEach(() => {
    findByPkStub = sinon.stub(Candidate, 'findByPk');
    createStub = sinon.stub(CourtSearch, 'create');
  });

  afterEach(() => {
    sinon.restore();
  });

  describe('getCourtSearchByCandidateId', () => {
    it('should return the court search if found', async () => {
      const courtSearch = {
        id: 1,
        search: 'search details',
        status: 'completed',
        date: new Date(),
      };
      const candidate = {
        id: 1,
        courtSearch
      };
      findByPkStub.resolves(candidate as Candidate);

      const result = await CourtSearchService.getCourtSearchByCandidateId(1);
      expect(result).to.equal(courtSearch);
    });

    it('should throw CandidateNotFoundException if candidate or court search not found', async () => {
      findByPkStub.resolves(null);
      await expect(CourtSearchService.getCourtSearchByCandidateId(1)).to.be.rejectedWith(CandidateNotFoundException, 'Candidate with id 1 not found');
    });
  });

  describe('createCourtSearch', () => {
    it('should create and return the new court search', async () => {
      const courtSearchData: CreateCourtSearchSchemaType = {
        search: 'search details',
        status: 'completed',
        date: '2024-05-22T14:20:00.000Z',
        candidateId: 1
      };

      const courtSearch = { id: 1, ...courtSearchData };
      createStub.resolves(courtSearch as unknown as CourtSearch);

      const result = await CourtSearchService.createCourtSearch(courtSearchData);
      expect(result).to.equal(courtSearch);
    });
  });
});
