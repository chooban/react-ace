/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import {
  mapDispatchToProps,
  __RewireAPI__
} from '../ProfileIcon';

import {
  logout,
  showSavedSearches
} from '../../actions/';

test('Profile icon', (t) => {
  t.test('Dispatches showSavedSearches', (t) => {
    const MockAuthService = {
      logout: sinon.spy()
    };
    const dispatchSpy = sinon.spy();
    __RewireAPI__.__Rewire__('AuthServiceFactory', () => MockAuthService);

    const props = mapDispatchToProps(dispatchSpy);
    props.displaySavedSearches();

    t.ok(dispatchSpy.calledOnce);
    t.ok(dispatchSpy.calledWith(showSavedSearches()));
    t.end();
  });

  t.test('Logs out from service and dispatches', (t) => {
    const MockAuthService = {
      logout: sinon.spy()
    };
    const dispatchSpy = sinon.spy();

    __RewireAPI__.__Rewire__('AuthServiceFactory', () => MockAuthService);

    const props = mapDispatchToProps(dispatchSpy);
    props.doLogout();

    t.ok(MockAuthService.logout.calledOnce);
    t.ok(dispatchSpy.calledOnce);
    t.ok(dispatchSpy.calledWith(logout()));

    t.end();
  });
});

