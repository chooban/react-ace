/* eslint no-shadow: 0 */
import test from 'blue-tape';
import thunk from 'redux-thunk';
import configureMockStore from 'redux-mock-store';
import * as Actions from '../';

const middlewares = [thunk];
const mockStore = configureMockStore(middlewares);

test('Adding to an order', (t) => {
  const lineItem = {
    previewsCode: '12345MAR'
  };

  const store = mockStore({});
  const expectedActions = [
    { type: 'ADD_TO_ORDER', orderItem: lineItem }
  ];

  store.dispatch(Actions.addToOrder(lineItem));

  t.deepEqual(store.getActions(), expectedActions);
  t.end();
});
