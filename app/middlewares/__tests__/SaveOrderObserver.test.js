/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import middleware from '../SaveOrderObserver';

test('Order saving middleware', (t) => {
  t.test('Should save when adding to order', (t) => {
    const order = {
      issue: 'ecmail333',
      items: ['a', 'b', 'c']
    };
    const fakeStore = {
      getState: () => ({ order })
    };
    const fakeNext = sinon.spy();
    const storage = {
      setItem: sinon.spy()
    };
    const action = {
      type: 'ADD_TO_ORDER',
      payload: null
    };
    const m = middleware(storage);

    m(fakeStore)(fakeNext)(action);

    t.ok(fakeNext.withArgs(action).calledOnce);
    t.ok(storage.setItem.withArgs('saved_order', JSON.stringify(order)));
    t.end();
  });
});
