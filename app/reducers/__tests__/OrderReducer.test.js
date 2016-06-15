/* eslint no-shadow: 0 */
import test from 'tape';
import * as Actions from '../../actions/ActionCreators';
import reducer from '../';

test('Order reducer functions', (t) => {
  const orderItem = {
    previewsCode: '332/0026',
    price: '6.99',
    publisher: 'DARK HORSE',
    reducedFrom: null,
    title: 'AVATAR LAST AIRBENDER TP 04 SEARCH PART 1'
  };

  t.test('should return the initial state', (t) => {
    const expectedInitialState = {
      issues: {
        isFetching: false,
        issuesList: [],
        data: []
      },
      order: {
        items: []
      }
    };

    t.deepEqual(
      reducer(undefined, {}),
      expectedInitialState,
      'Incorrect initial state');
    t.end();
  });

  t.test('adding a unique item to an empty order', (t) => {
    let state = reducer(undefined, {});
    state = reducer(state, Actions.addToOrder(orderItem));

    t.equal(state.order.items.size, 1);
    t.equal(state.order.items.has(orderItem), true);
    t.end();
  });

  t.test('cannot add the same item twice', (t) => {
    let state = reducer(undefined, {});
    state = reducer(state, Actions.addToOrder(orderItem));
    state = reducer(state, Actions.addToOrder(orderItem));

    t.equal(state.order.items.size, 1);
    t.equal(state.order.items.has(orderItem), true);
    t.end();
  });

  t.test('can remove items from order', (t) => {
    let state = reducer(undefined, {});
    state = reducer(state, Actions.addToOrder(orderItem));
    state = reducer(state, Actions.removeFromOrder(orderItem));

    t.equal(state.order.items.size, 0);
    t.equal(state.order.items.has(orderItem), false);
    t.end();
  });
});
