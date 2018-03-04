/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import { showOrder } from '../../actions';

import {
  mapStateToProps,
  mapDispatchToProps
} from '../ShoppingCartContainer';

test('Shopping Cart container', (t) => {
  t.test('onClick dispatches show order actions', (t) => {
    const dispatchSpy = sinon.spy();

    const props = mapDispatchToProps(dispatchSpy);

    props.onClick();

    t.ok(dispatchSpy.calledOnce);
    t.ok(dispatchSpy.calledWith(showOrder()));
    t.end();
  });

  t.test('Count with no order items', (t) => {
    const state = {
      order: {
        items: []
      }
    };
    const props = mapStateToProps(state);

    t.equal(props.iconName, 'shopping_cart');
    t.equal(props.count, 0);
    t.end();
  });

  t.test('Count with order items', (t) => {
    const state = {
      order: {
        items: ['a']
      }
    };
    const props = mapStateToProps(state);

    t.equal(props.iconName, 'shopping_cart');
    t.equal(props.count, 1);
    t.end();
  });
});
