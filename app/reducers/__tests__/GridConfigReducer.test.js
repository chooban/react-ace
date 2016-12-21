/* eslint no-shadow: 0 */
import test from 'tape';
import * as Actions from '../../actions/ActionCreators';
import reducer from '../';

test('Grid config reducer functions', (t) => {
  t.test('Next page', (t) => {
    let state = reducer(undefined, {});
    state = reducer(state, Actions.nextPage());

    t.equal(state.gridConfig.page, 2);
    t.end();
  });

  t.test('Previous page has floor of zero', (t) => {
    let state = reducer(undefined, {});
    state = reducer(state, Actions.previousPage());

    t.equal(state.gridConfig.page, 1);
    t.end();
  });

  t.test('Previous page decrements page number', (t) => {
    let state = reducer(undefined, {});
    state.gridConfig.page = 5;
    state = reducer(state, Actions.previousPage());

    t.equal(state.gridConfig.page, 4);
    t.end();
  });
});
