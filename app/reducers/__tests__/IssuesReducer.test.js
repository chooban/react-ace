/* eslint no-shadow: 0 */
import test from 'tape';
import * as Actions from '../../actions/ActionCreators';
import reducer from '../';

test('Issues reducer', (t) => {
  const initialState = reducer(undefined, {});
  const issues = [331, 332, 333];

  t.test('Requesting the list of issues', (t) => {
    const state = reducer(initialState, Actions.requestedIssues());

    t.equal(state.issues.isFetching, true, 'Sets the fetching flag');
    t.end();
  });

  t.test('Receiving the list of issues', (t) => {
    let state = reducer(initialState, Actions.requestedIssues());
    state = reducer(state, Actions.receivedIssues(issues));

    t.deepEqual(state.issues.issuesList, issues);
    t.equal(state.issues.isFetching, false);
    t.end();
  });

  t.test('Requesting an issue', (t) => {
    const state = reducer(initialState, Actions.requestedIssue());

    t.equal(state.issues.isFetching, true, 'Sets the fetching flag');
    t.end();
  });

  t.test('Receiving an issue', (t) => {
    const issue = [];
    let state = reducer(initialState, Actions.requestedIssue(331));
    state = reducer(state, Actions.receivedIssue(issue));

    t.equal(state.issues.isFetching, false);
    t.deepEqual(state.issues.data, issue);
    t.end();
  });
});
