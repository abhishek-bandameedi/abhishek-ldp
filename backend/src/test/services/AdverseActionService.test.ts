import chai, { expect } from 'chai';
import sinon from 'sinon';
import chaiAsPromised from 'chai-as-promised';
import { AdverseAction } from '../../models/AdverseAction';
import { AdverseActionService } from '../../services/AdverseActionService';
import { CreateAdverseActionSchemaType } from '../../utils/validations';

chai.use(chaiAsPromised);

describe('AdverseActionService', () => {
  let findAndCountAllStub: sinon.SinonStub;
  let createStub: sinon.SinonStub;

  beforeEach(() => {
    findAndCountAllStub = sinon.stub(AdverseAction, 'findAndCountAll');
    createStub = sinon.stub(AdverseAction, 'create');
  });

  afterEach(() => {
    sinon.restore();
  });

  describe('getAllAdverseActions', () => {
    it('should return paginated adverse actions', async () => {
      const adverseActions = [{ id: 1, status: 'pending', pre_notice_date: new Date(), post_notice_date: new Date() }];
      const count = 1;

      findAndCountAllStub.resolves({ count, rows: adverseActions });

      const page = 1;
      const size = 10;

      const result = await AdverseActionService.getAllAdverseActions(page, size);

      expect(result.totalItems).to.equal(count);
      expect(result.totalPages).to.equal(Math.ceil(count / size));
      expect(result.currentPage).to.equal(page);
      expect(result.adverseActions).to.equal(adverseActions);
    });
  });

  describe('createAdverseAction', () => {
    it('should create and return the new adverse action', async () => {
      const adverseActionData: CreateAdverseActionSchemaType = {
        status: 'pending',
        pre_notice_date: '2024-05-22T14:20:00.000Z',
        post_notice_date: '2024-05-22T14:20:00.000Z',
        candidateId: 1
      };

      const adverseAction = { id: 1, ...adverseActionData };
      createStub.resolves(adverseAction as unknown as AdverseAction);

      const result = await AdverseActionService.createAdverseAction(adverseActionData);
      expect(result).to.equal(adverseAction);
    });
  });
});
