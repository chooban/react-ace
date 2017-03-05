/* eslint no-shadow: 0 */
import test from 'blue-tape';
import thunk from 'redux-thunk';
import configureMockStore from 'redux-mock-store';

import { addNewSavedSearch, __RewireAPI__ as ActionsRewireAPI } from '../';

const middlewares = [thunk];
const mockStore = configureMockStore(middlewares);

test('Saved searches actions', (t) => {
  t.test('Add new saved search', (t) => {
    const preProfile = {
      user_metadata: {
        saved_searches: [
          'dredd'
        ]
      }
    };

    const postProfile = {
      user_metadata: {
        saved_searches: [
          'dredd',
          'foo'
        ]
      }
    };

    const expectedActions = [
      {
        type: 'ADD_SAVED_SEARCH',
        payload: 'foo'
      },
      {
        type: 'SET_USER_PROFILE',
        payload: postProfile
      }
    ];

    ActionsRewireAPI.__Rewire__('updateProfile', (p) => (
      Promise.resolve(p)
    ));

    const store = mockStore({
      user: {
        profile: preProfile
      }
    });

    return store.dispatch(addNewSavedSearch('foo'))
      .then(() => {
        t.deepEqual(store.getActions(), expectedActions, 'Expected actions match');
        ActionsRewireAPI.__ResetDependency__('updateProfile');
      });
  });
});
