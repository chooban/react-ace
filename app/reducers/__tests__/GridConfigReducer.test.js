/* eslint no-shadow: 0 */
import test from 'tape';
import * as Actions from '../../actions/';
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

  ['UPDATE_SEARCH', 'PERFORM_SAVED_SEARCH'].forEach((actionType) => {
    t.test(`First search term resets page number: ${actionType}`, (t) => {
      let state = reducer({
        gridConfig: {
          page: 5,
          searchTerm: undefined,
          pageSize: 25
        }
      }, {});

      state = reducer(state, {
        type: actionType,
        payload: 'marvel'
      });

      t.equal(state.gridConfig.searchTerm, 'marvel');
      t.equal(state.gridConfig.page, 1);
      t.end();
    });

    t.test('Removing search term resets page number', (t) => {
      let state = reducer({
        gridConfig: {
          page: 5,
          searchTerm: 'marvel',
          pageSize: 25
        }
      }, {});

      state = reducer(state, {
        type: actionType,
        payload: undefined
      });

      t.equal(state.gridConfig.searchTerm, undefined);
      t.equal(state.gridConfig.page, 1);
      t.end();
    });

    t.test('Trailing spaces are removed', (t) => {
      let state = reducer({
        gridConfig: {
          page: 5,
          searchTerm: 'marvel',
          pageSize: 25
        }
      }, {});

      state = reducer(state, {
        type: actionType,
        payload: 'marvel  '
      });

      t.equal(state.gridConfig.searchTerm, 'marvel');
      t.equal(state.gridConfig.page, 5);
      t.end();
    });

    t.test('Leading spaces are removed', (t) => {
      let state = reducer({
        gridConfig: {
          page: 5,
          searchTerm: 'marvel',
          pageSize: 25
        }
      }, {});

      state = reducer(state, {
        type: actionType,
        payload: '  marvel'
      });

      t.equal(state.gridConfig.searchTerm, 'marvel');
      t.equal(state.gridConfig.page, 5);
      t.end();
    });

    t.test('Empty string is a reset', (t) => {
      let state = reducer({
        gridConfig: {
          page: 5,
          searchTerm: 'marvel',
          pageSize: 25
        }
      }, {});

      state = reducer(state, {
        type: actionType,
        payload: ''
      });

      t.equal(state.gridConfig.searchTerm, undefined);
      t.equal(state.gridConfig.page, 1);
      t.end();
    });
  });
});
