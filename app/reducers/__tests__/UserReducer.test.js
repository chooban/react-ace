/* eslint no-shadow: 0 */
import test from 'tape';
import reducer from '../';

test('User profile reducer functions', (t) => {
  const profile = {
    username: 'chooban'
  };

  const hardcodedSearches = [
    'rick',
    'bad machinery',
    'tmnt',
    'conan',
    'ms marvel',
    'hulk',
    'harrow county tp',
    'spiderman',
    'clean room'
  ];

  const profileWithSearches = Object.assign({}, profile, {
    savedsearches: hardcodedSearches
  });

  t.test('Setting the user profile', (t) => {
    let state = reducer(undefined, {});
    state = reducer(state, {
      type: 'SET_USER_PROFILE',
      payload: profile
    });

    t.deepEqual(state.user.profile, profileWithSearches);
    t.end();
  });

  t.test('Logging out', (t) => {
    let state = reducer(undefined, {});
    state = reducer(state, {
      type: 'SET_USER_PROFILE',
      payload: profile
    });
    state = reducer(state, {
      type: 'LOGOUT'
    });

    t.notOk(state.user.profile);
    t.end();
  });

  t.test('Removing a saved search', (t) => {
    let state = reducer(undefined, {});
    state = reducer(state, {
      type: 'SET_USER_PROFILE',
      payload: profile
    });

    const numberOfSearches = state.user.profile.savedsearches.length;

    t.equal(state.user.profile.savedsearches.includes('bad machinery'), true);

    state = reducer(state, {
      type: 'DELETE_SAVED_SEARCH',
      payload: 'bad machinery'
    });

    t.equal(state.user.profile.savedsearches.includes('bad machinery'), false);
    t.equal(state.user.profile.savedsearches.length, numberOfSearches - 1);
    t.end();
  });
});
