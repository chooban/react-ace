/* eslint no-shadow: 0 */
import test from 'tape';
import reducer from '../';

test('User profile reducer functions', (t) => {
  const profile = {
    username: 'chooban',
    savedsearches: [
      'rick',
      'bad machinery'
    ]
  };

  t.test('Setting the user profile', (t) => {
    let state = reducer(undefined, {});
    state = reducer(state, {
      type: 'SET_USER_PROFILE',
      payload: profile
    });

    t.deepEqual(state.user.profile, profile);
    t.end();
  });

  t.test('Logging out', (t) => {
    let state = reducer(undefined, {});
    state = reducer(state, {
      type: 'SET_USER_PROFILE',
      payload: profile
    });

    t.deepEqual(state.user.profile, profile);
    state = reducer(state, {
      type: 'LOGOUT'
    });
    t.end();
  });

  t.test('Removing a saved search', (t) => {
    let state = reducer(undefined, {});
    state = reducer(state, {
      type: 'SET_USER_PROFILE',
      payload: profile
    });
    state = reducer(state, {
      type: 'DELETE_SAVED_SEARCH',
      payload: 'bad machinery'
    });

    t.deepEqual(state.user.profile.savedsearches, ['rick']);
    t.end();
  });
});
