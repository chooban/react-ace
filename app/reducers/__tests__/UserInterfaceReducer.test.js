/* eslint no-shadow: 0 */
import test from 'tape';

import reducer from '../';
import * as Actions from '../../actions/';

test('User interface reducer functions', (t) => {
  const actionsToTest = [
    {
      key: 'showOrder',
      trueAction: Actions.showOrder(),
      falseAction: Actions.closeOrder()
    },
    {
      key: 'showHelp',
      trueAction: Actions.showHelp(),
      falseAction: Actions.closeHelp()
    },
    {
      key: 'showItemPreview',
      trueAction: Actions.showPreview(),
      falseAction: Actions.closePreview()
    },
    {
      key: 'showSavedSearches',
      trueAction: Actions.showSavedSearches(),
      falseAction: Actions.closeSavedSearches()
    }
  ];

  actionsToTest.forEach((a) => {
    t.test(`UI flag: ${a.key}`, (t) => {
      let state = reducer(undefined, {});
      t.equal(state.ui[a.key], false);

      state = reducer(state, a.trueAction);
      t.equal(state.ui[a.key], true);

      state = reducer(state, a.falseAction);
      t.equal(state.ui[a.key], false);

      t.end();
    });
  });

  // Skipped as the action is an async thunk. Needs more work.
  t.skip('Adding to order closes preview', (t) => {
    let state = reducer(undefined, {});
    state.ui.showItemPreview = true;

    state = reducer(state, Actions.addToOrder());
    t.notOk(state.ui.showItemPreview);
    t.end();
  });

  t.test('Removing from order closes preview', (t) => {
    let state = reducer(undefined, {});
    state.ui.showItemPreview = true;

    state = reducer(state, Actions.removeFromOrder());
    t.equal(state.ui.showItemPreview, false);
    t.end();
  });

  t.test('Exporting order closes order popup', (t) => {
    let state = reducer(undefined, {});
    state.ui.showOrder = true;

    state = reducer(state, Actions.exportOrder());
    t.notOk(state.ui.showOrder);
    t.end();
  });

  t.test('Closing the order...closes it', (t) => {
    let state = reducer(undefined, {});
    state.ui.showOrder = true;

    state = reducer(state, Actions.closeOrder());
    t.notOk(state.ui.showOrder);
    t.end();
  });
});
