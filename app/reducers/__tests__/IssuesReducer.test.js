/* eslint no-shadow: 0 */
import test from 'tape';
import * as Actions from '../../actions/';
import reducer from '../';

test('Issues reducer', (t) => {
  const initialState = reducer(undefined, {});

  t.test('Requesting an issue', (t) => {
    const state = reducer(initialState, Actions.requestedIssue());

    t.equal(state.issues.isFetching, true, 'Sets the fetching flag');
    t.end();
  });

  t.test('Receiving an issue', (t) => {
    const issue = {
      file: 'ecmail332',
      contents: []
    };
    let state = reducer(initialState, Actions.requestedIssue(331));
    state = reducer(state, Actions.receivedIssue(issue));

    t.equal(state.issues.isFetching, false);
    t.deepEqual(state.issues.data, []);
    t.end();
  });
});
