/* eslint no-shadow: 0 */
import test from 'blue-tape';
import thunk from 'redux-thunk';
import configureMockStore from 'redux-mock-store';
import fetchMock from 'fetch-mock';
import * as Actions from '../';

const middlewares = [thunk];
const mockStore = configureMockStore(middlewares);

test('Issues Actions', (t) => {
  t.test('Requesting the latest issue', (t) => {
    const apiURL = '/api/previews/latest';
    fetchMock
      .get(apiURL, '{"contents": []}');

    const store = mockStore({});
    const expectedActions = [
      { type: 'REQUESTED_ISSUE_DATA' },
      { type: 'RECEIVED_ISSUE_DATA', payload: { contents: [] } }
    ];

    return store.dispatch(Actions.requestLatestIssue())
      .then(() => {
        t.deepEqual(store.getActions(), expectedActions, 'Expected actions match');
        t.equal(fetchMock.called(apiURL), true, 'Web API was called');
        t.equal(fetchMock.calls().unmatched.length, 0, 'No unexpected web requests');
        fetchMock.restore();
      });
  });
});
