/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import initialState from '../InitialState';
import reducer, { __RewireAPI__ as ReducerRewireAPI } from '../ProfileReducer';

test('User profile reducer functions', (t) => {
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

  const auth0ProfileNoSearches = {
    clientID: 'Cqh6CnKuIrfK7D3ZRxcpS',
    nickname: 'chooban',
    created_at: '2017-01-30T14:55:59.681Z'
  };

  const auth0ProfileWithSearches = Object.assign({}, auth0ProfileNoSearches, {
    user_metadata: {
      saved_searches: hardcodedSearches
    }
  });

  t.test('Setting the user profile without searches', (t) => {
    let state = reducer(initialState.user, {});
    state = reducer(state, {
      type: 'SET_USER_PROFILE',
      payload: auth0ProfileNoSearches
    });

    t.deepEqual(state.profile, {
      nickname: 'chooban',
      savedsearches: []
    });
    t.ok(state.profileFetched);
    t.end();
  });

  t.test('Profile with searches', (t) => {
    let state = reducer(undefined, {});
    state = reducer(state, {
      type: 'SET_USER_PROFILE',
      payload: auth0ProfileWithSearches
    });

    t.deepEqual(state.profile, {
      nickname: 'chooban',
      savedsearches: hardcodedSearches
    });
    t.ok(state.profileFetched);
    t.end();
  });

  t.test('Logging out', (t) => {
    const AuthService = {
      logout: sinon.spy()
    };
    ReducerRewireAPI.__Rewire__('AuthServiceFactory', () => AuthService);
    let state = reducer(undefined, {});
    state = reducer(state, {
      type: 'SET_USER_PROFILE',
      payload: auth0ProfileNoSearches
    });

    state = reducer(state, {
      type: 'LOGOUT'
    });
    ReducerRewireAPI.__ResetDependency__('AuthServiceFactory');
    t.ok(AuthService.logout.calledOnce);
    t.notOk(state.profile);
    t.notOk(state.profileFetched);
    t.end();
  });

  t.test('Removing a saved search', (t) => {
    let state = reducer(undefined, {});
    state = reducer(state, {
      type: 'SET_USER_PROFILE',
      payload: auth0ProfileWithSearches
    });

    const numberOfSearches = state.profile.savedsearches.length;
    t.equal(state.profile.savedsearches.includes('bad machinery'), true);

    state = reducer(state, {
      type: 'DELETE_SAVED_SEARCH',
      payload: 'bad machinery'
    });

    t.equal(state.profile.savedsearches.includes('bad machinery'), false);
    t.equal(state.profile.savedsearches.length, numberOfSearches - 1);
    t.end();
  });

  t.test('Removing a non-existent saved search', (t) => {
    let state = reducer(undefined, {});
    state = reducer(state, {
      type: 'SET_USER_PROFILE',
      payload: auth0ProfileWithSearches
    });

    const numberOfSearches = state.profile.savedsearches.length;

    state = reducer(state, {
      type: 'DELETE_SAVED_SEARCH',
      payload: 'flubber'
    });

    t.equal(state.profile.savedsearches.length, numberOfSearches);
    t.end();
  });

  t.test('Adding a saved search', (t) => {
    let state = reducer(undefined, {});
    state = reducer(state, {
      type: 'SET_USER_PROFILE',
      payload: auth0ProfileNoSearches
    });

    const numberOfSearches = state.profile.savedsearches.length;
    t.equal(state.profile.savedsearches.includes('northlanders'), false);

    state = reducer(state, {
      type: 'ADD_SAVED_SEARCH',
      payload: 'northlanders'
    });

    t.equal(state.profile.savedsearches.includes('northlanders'), true);
    t.equal(state.profile.savedsearches.length, numberOfSearches + 1);
    t.end();
  });

  t.test('Adding a duplicate saved search', (t) => {
    let state = reducer(undefined, {});
    state = reducer(state, {
      type: 'SET_USER_PROFILE',
      payload: auth0ProfileNoSearches
    });

    const numberOfSearches = state.profile.savedsearches.length;
    t.equal(state.profile.savedsearches.includes('northlanders'), false);

    state = reducer(state, {
      type: 'ADD_SAVED_SEARCH',
      payload: 'northlanders'
    });

    t.equal(state.profile.savedsearches.includes('northlanders'), true);
    t.equal(state.profile.savedsearches.length, numberOfSearches + 1);

    state = reducer(state, {
      type: 'ADD_SAVED_SEARCH',
      payload: 'northlanders'
    });

    t.equal(state.profile.savedsearches.length, numberOfSearches + 1);
    t.end();
  });
});
