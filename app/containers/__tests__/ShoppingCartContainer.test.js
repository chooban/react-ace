/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import * as actions from '../../actions';

import {
  mapStateToProps,
  mapDispatchToProps
} from '../ShoppingCartContainer';

test('Shopping Cart container', (t) => {
  t.test('Dispatches show order actions', (t) => {
    const dispatchSpy = sinon.spy();
    const actionSpy = sinon.spy(actions, 'showOrder');

    const props = mapDispatchToProps(dispatchSpy);

    props.showCurrentOrder();

    t.ok(dispatchSpy.calledOnce);
    t.ok(actionSpy.calledOnce);

    t.end();
  });

  t.test('Extracts order from the state', (t) => {
    const items = [1, 2, 3];
    const state = {
      order: {
        items
      }
    };

    const props = mapStateToProps(state);

    t.equal(props.items, items);
    t.end();
  });
});
