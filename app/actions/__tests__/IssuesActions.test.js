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
      .get('/api/previews/', '[331, 332, 333]');

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

  t.test('Requesting a single issue', (t) => {
    const apiURL = '/api/previews/333';
    fetchMock
      .get(apiURL, '{"contents": {}}');

    const store = mockStore({});
    const expectedActions = [
      { type: 'REQUESTED_ISSUE_DATA', issueNumber: 333 },
      { type: 'RECEIVED_ISSUE_DATA', issueData: {}
      }
    ];

    return store.dispatch(Actions.requestIssue(333))
      .then(() => {
        t.deepEqual(store.getActions(), expectedActions, 'Expected actions match');
        t.equal(fetchMock.called(apiURL), true, 'Web API was called');
        t.equal(fetchMock.calls().unmatched.length, 0, 'No unexpected web requests');
        fetchMock.restore();
      });
  });

  t.test('Requesting the latest issue', (t) => {
    const apiURL = '/api/previews/latest';
    fetchMock
      .get(apiURL, '{"contents": {}}');

    const store = mockStore({});
    const expectedActions = [
      { type: 'RECEIVED_ISSUE_DATA', issueData: {} }
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
