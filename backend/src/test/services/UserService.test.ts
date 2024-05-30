import { expect } from 'chai';
import sinon from 'sinon';
import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';
import { User } from '../../models/User';
import * as UserService from '../../services/UserService';
import InvalidCredentialsException from '../../exceptions/InvalidCredentialException';

describe('UserService', () => {
  let bcryptHashStub: sinon.SinonStub;
  let bcryptCompareStub: sinon.SinonStub;
  let jwtSignStub: sinon.SinonStub;
  let userFindOneStub: sinon.SinonStub;
  let userCreateStub: sinon.SinonStub;

  beforeEach(() => {
    bcryptHashStub = sinon.stub(bcrypt, 'hash');
    bcryptCompareStub = sinon.stub(bcrypt, 'compare');
    jwtSignStub = sinon.stub(jwt, 'sign');
    userFindOneStub = sinon.stub(User, 'findOne');
    userCreateStub = sinon.stub(User, 'create');
  });

  afterEach(() => {
    sinon.restore();
  });

  describe('signUpUser', () => {
    it('should create a new user with hashed password', async () => {
      const signUpData = { email: 'test@example.com', password: 'password123' };
      const hashedPassword = 'hashedpassword';
      const createdUser = { id: 1, email: signUpData.email, password: hashedPassword };

      bcryptHashStub.resolves(hashedPassword);
      userCreateStub.resolves(createdUser);

      const result = await UserService.signUpUser(signUpData);

      expect(bcryptHashStub.calledOnceWith(signUpData.password, 12)).to.be.true;
      expect(userCreateStub.calledOnceWith({ email: signUpData.email, password: hashedPassword })).to.be.true;
      expect(result).to.deep.equal(createdUser);
    });
  });

  describe('loginUser', () => {
    it('should throw InvalidCredentialsException if user is not found', async () => {
      const loginData = { email: 'nonexistent@example.com', password: 'password123' };
      userFindOneStub.resolves(null);

      try {
        await UserService.loginUser(loginData);
      } catch (error) {
        expect(error).to.be.instanceOf(InvalidCredentialsException);
      }

      expect(userFindOneStub.calledOnceWith({ where: { email: loginData.email } })).to.be.true;
    });

    it('should throw InvalidCredentialsException if password does not match', async () => {
      const loginData = { email: 'test@example.com', password: 'wrongpassword' };
      const user = { id: 1, email: loginData.email, password: 'hashedpassword' };

      userFindOneStub.resolves(user);
      bcryptCompareStub.resolves(false);

      try {
        await UserService.loginUser(loginData);
      } catch (error) {
        expect(error).to.be.instanceOf(InvalidCredentialsException);
      }

      expect(userFindOneStub.calledOnceWith({ where: { email: loginData.email } })).to.be.true;
      expect(bcryptCompareStub.calledOnceWith(loginData.password, user.password)).to.be.true;
    });

    it('should return user and token if login is successful', async () => {
      const loginData = { email: 'test@example.com', password: 'password123' };
      const user = { id: 1, email: loginData.email, password: 'hashedpassword' };
      const token = 'jsonwebtoken';

      userFindOneStub.resolves(user);
      bcryptCompareStub.resolves(true);
      jwtSignStub.returns(token);

      const result = await UserService.loginUser(loginData);

      expect(userFindOneStub.calledOnceWith({ where: { email: loginData.email } })).to.be.true;
      expect(bcryptCompareStub.calledOnceWith(loginData.password, user.password)).to.be.true;
      expect(jwtSignStub.calledOnce).to.be.true;
      expect(result).to.deep.equal({ user, token });
    });
  });
});
