/* eslint no-shadow: 0 */
import test from 'tape';
import * as Actions from '../../actions/';
import reducer from '../';

test('Order reducer functions', (t) => {
  const previewsCode = '332/0026';
  const orderItem = {
    previews: previewsCode,
    quantity: 1,
    title: 'Spider-Man',
    publisher: 'Marvel',
    comment: '',
    price: 2.5
  };

  t.test('adding a unique item to an empty order', (t) => {
    let state = reducer(undefined, {});
    state = reducer(state, {
      type: 'ADD_TO_ORDER',
      payload: orderItem
    });

    t.equal(state.order.items.length, 1);
    t.equal(state.order.items.findIndex((d) => d.previews === previewsCode), 0);
    t.equal(state.order.total, 2.5);
    t.end();
  });

  t.test('cannot add the same item twice', (t) => {
    let state = reducer(undefined, {});
    state = reducer(state, {
      type: 'ADD_TO_ORDER',
      payload: orderItem
    });
    state = reducer(state, {
      type: 'ADD_TO_ORDER',
      payload: orderItem
    });

    t.equal(state.order.items.length, 1);
    t.equal(state.order.total, 2.5);
    t.end();
  });

  t.test('can remove items from order', (t) => {
    let state = reducer(undefined, {});
    state = reducer(state, {
      type: 'ADD_TO_ORDER',
      payload: orderItem
    });
    t.equal(state.order.items.length, 1);
    state = reducer(state, Actions.removeFromOrder(previewsCode));
    t.equal(state.order.items.length, 0);
    t.equal(state.order.total, 0);
    t.end();
  });

  t.test('receiving an issue sets the order number', (t) => {
    const issue = {
      file: 'ecmail332',
      contents: [{
        previewsCode: '332/0026',
        price: 6.99,
        publisher: 'DARK HORSE',
        reducedFrom: null,
        title: 'AVATAR LAST AIRBENDER TP 04 SEARCH PART 1'
      }]
    };
    const state = reducer(undefined, Actions.receivedIssue(issue));
    t.equal(state.order.issue, 'ecmail332');
    t.end();
  });

  t.test('Clearing an order', (t) => {
    let state = reducer(undefined, {});
    state.order = {
      issue: 'ecmail331',
      items: ['abc']
    };

    state = reducer(state, Actions.clearOrder());

    t.notOk(state.order.issue);
    t.equal(state.order.items.length, 0);
    t.end();
  });
});
