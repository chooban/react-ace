/* eslint no-shadow: 0 */
import fetchMock from 'fetch-mock';
import test from 'tape';

import { updateProfile, __RewireAPI__ as ProfilesRewireAPI } from '../ProfilesWebApi';

const searches = [
  'dredd',
  'anderson'
];

const AuthService = {
  getToken: function getToken() {
    return 'abc';
  }
};

test('Profiles API', (t) => {
  t.test('Update user profile', (t) => {
    ProfilesRewireAPI.__Rewire__('AuthServiceFactory', () => AuthService);
    fetchMock.post('*', JSON.stringify('ok'));

    return updateProfile(searches).then(() => {
      const configUsed = fetchMock.lastOptions();
      t.equal(configUsed.method, 'POST');
      t.equal(configUsed.body, '["dredd","anderson"]');
      t.equal(configUsed.headers.Authorization, 'Bearer abc');
      t.ok(true);
      fetchMock.restore();
      ProfilesRewireAPI.__ResetDependency__('AuthServiceFactory');
    });
  });

  t.test('Errors propagate', (t) => {
    ProfilesRewireAPI.__Rewire__('AuthServiceFactory', () => AuthService);
    fetchMock.post('*', 500);

    return updateProfile(searches).then(() => {
      fetchMock.restore();
      ProfilesRewireAPI.__ResetDependency__('AuthServiceFactory');
      t.fail('Should have thrown an error');
    }).catch((d) => {
      fetchMock.restore();
      ProfilesRewireAPI.__ResetDependency__('AuthServiceFactory');
      t.ok(d instanceof Error, 'Was not an error');
    });
  });
});
