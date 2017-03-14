/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import {
  mapStateToProps,
  __RewireAPI__
} from '../LoginIcon';

test('Login Icon', (t) => {
  t.test('Invokes lock on click', (t) => {
    const MockAuthService = {
      login: sinon.spy()
    };
    const MockServiceFactory = () => MockAuthService;
    __RewireAPI__.__Rewire__('AuthServiceFactory', MockServiceFactory);

    const props = mapStateToProps();
    props.onClick();

    t.ok(MockAuthService.login.calledOnce);
    t.end();

    __RewireAPI__.__ResetDependency__('AuthServiceFactory');
  });
});
