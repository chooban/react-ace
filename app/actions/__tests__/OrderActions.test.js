/* eslint no-shadow: 0 */
import test from 'blue-tape';
import thunk from 'redux-thunk';
import configureMockStore from 'redux-mock-store';
import * as Actions from '../';

const middlewares = [thunk];
const mockStore = configureMockStore(middlewares);

test('Adding to an order', (t) => {
  const lineItem = {
    previews: '123/MAR',
    publisher: 'foo',
    title: 'bar',
    price: 0,
    quantity: 1,
    comment: ''
  };

  const store = mockStore({
    issues: {
      data: [{
        previewsCode: '123/MAR',
        publisher: 'foo',
        title: 'bar',
        price: 0
      }]
    },
    order: {
      items: []
    }
  });
  const expectedActions = [
    { type: 'ADD_TO_ORDER', payload: lineItem }
  ];

  store.dispatch(Actions.addToOrder(lineItem.previews));
  t.deepEqual(store.getActions(), expectedActions);
  t.end();
});
