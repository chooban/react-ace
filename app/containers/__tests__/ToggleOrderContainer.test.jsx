/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import * as actions from '../../actions';

import {
  mapStateToProps,
  mapDispatchToProps
} from '../ToggleOrderContainer';

test('Toggle Order Container', (t) => {
  t.test('Adds to order if selected item is not ordered', (t) => {
    const dispatchSpy = sinon.spy();
    const addToOrderSpy = sinon.spy(actions, 'addToOrder');
    const props = mapDispatchToProps(dispatchSpy);

    props.onItemSelected('ABC/1234', false);

    t.equal(dispatchSpy.calledOnce, true);

    t.equal(addToOrderSpy.calledOnce, true);
    t.equal(addToOrderSpy.calledWith('ABC/1234'), true);
    t.end();
  });

  t.test('Removes from order if selected item is ordered', (t) => {
    const dispatchSpy = sinon.spy();
    const actionSpy = sinon.spy(actions, 'removeFromOrder');
    const props = mapDispatchToProps(dispatchSpy);

    props.onItemSelected('ABC/1234', true);
    t.equal(dispatchSpy.calledOnce, true);
    t.equal(actionSpy.calledOnce, true);
    t.end();
  });

  t.test('Flagged as ordered if in the order', (t) => {
    const state = {
      order: {
        items: [
          { previews: '340/0078' },
          { previews: '340/0082' },
          { previews: '340/0056' }
        ]
      }
    };

    const props = mapStateToProps(state, { previewsCode: '340/0082' });

    t.ok(props.ordered, 'Should be ordered');
    t.end();
  });
});
