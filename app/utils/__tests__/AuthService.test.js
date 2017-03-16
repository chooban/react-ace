/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import {
  AuthServiceFactory,
  AuthService,
  __RewireAPI__ } from '../AuthService';

test('Auth service', (t) => {
  t.test('Login defers to lock', (t) => {
    const lock = {
      on: sinon.spy(),
      show: sinon.spy()
    };
    const service = new AuthService(lock, {});
    service.login();
    t.ok(lock.show.calledOnce);
    t.end();
  });

  t.test('Setting the token', (t) => {
    const mockStorage = {
      setItem: sinon.spy(),
      getItem: sinon.spy()
    };
    const lock = {
      on: sinon.spy(),
      show: sinon.spy()
    };

    const service = new AuthService(lock, mockStorage);
    service.setToken('ABC1234');

    t.ok(mockStorage.setItem.calledOnce);
    t.ok(mockStorage.setItem.calledWith('id_token', 'ABC1234'));
    t.end();
  });

  t.test('Getting the token', (t) => {
    const mockStorage = {
      setItem: sinon.spy(),
      getItem: sinon.stub().returns('ABC1234')
    };
    const lock = {
      on: sinon.spy(),
      show: sinon.spy()
    };

    const service = new AuthService(lock, mockStorage);
    const token = service.getToken();

    t.equal(token, 'ABC1234');
    t.ok(mockStorage.getItem.calledOnce);
    t.ok(mockStorage.getItem.calledWith('id_token'));
    t.end();
  });

  t.test('Logging out', (t) => {
    const lock = {
      on: sinon.spy()
    };
    const mockStorage = {
      removeItem: sinon.spy()
    };

    const service = new AuthService(lock, mockStorage);
    service.logout();
    t.ok(mockStorage.removeItem.calledOnce);
    t.ok(mockStorage.removeItem.calledWith('id_token'));
    t.end();
  });

  t.test('Not logged in', (t) => {
    const lock = { on: sinon.spy() };
    const mockStorage = {
      getItem: sinon.stub().returns(null)
    };
    const service = new AuthService(lock, mockStorage);
    t.notOk(service.loggedIn());
    t.ok(mockStorage.getItem.calledOnce);
    t.ok(mockStorage.getItem.calledWith('id_token'));
    t.end();
  });

  t.test('Logged in', (t) => {
    const lock = { on: sinon.spy() };
    const mockStorage = {
      getItem: sinon.stub().returns('ABC1234')
    };
    const service = new AuthService(lock, mockStorage);
    t.ok(service.loggedIn());
    t.ok(mockStorage.getItem.calledOnce);
    t.ok(mockStorage.getItem.calledWith('id_token'));
    t.end();
  });

  // XXX The Lock object needs a DOM
  t.skip('Factory function', (t) => {
    const config = {
      auth0Id: 'abc',
      auth0Domain: 'abc'
    };

    __RewireAPI__.__RewireDependency__('config', config);
    const serviceA = AuthServiceFactory();
    const serviceB = AuthServiceFactory();

    t.equal(serviceA, serviceB);
    t.end();

    __RewireAPI__.__ResetDependency__('config');
  });

  // TODO Work out local storage testing
});
