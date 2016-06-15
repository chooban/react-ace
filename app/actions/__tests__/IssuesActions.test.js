/* eslint no-shadow: 0 */
import test from 'blue-tape';
import thunk from 'redux-thunk';
import configureMockStore from 'redux-mock-store';
import fetchMock from 'fetch-mock';
import * as Actions from '../';

const middlewares = [thunk];
const mockStore = configureMockStore(middlewares);

test('Issues Actions', (t) => {
  t.test('Requesting issues', (t) => {
    fetchMock
      .mock('/api/previews/', 'GET', '[331, 332, 333]');

    const store = mockStore({});
    const expectedActions = [
      { type: 'REQUESTED_ISSUES' },
      { type: 'RECEIVED_ISSUES',
        issues: [331, 332, 333]
      }
    ];

    return store.dispatch(Actions.requestIssues())
      .then(() => {
        t.deepEqual(store.getActions(), expectedActions);
        t.equal(fetchMock.called('/api/previews/'), true);
        t.equal(fetchMock.calls().unmatched.length, 0);
        fetchMock.restore();
      });
  });
});
