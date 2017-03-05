/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import { AuthService } from '../AuthService';

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

  // TODO Work out local storage testing
});
