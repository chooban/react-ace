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
    const service = new AuthService(lock);
    service.login();
    t.ok(lock.show.calledOnce);
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
