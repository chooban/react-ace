/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import {
  removeFromOrder
} from '../../actions';

import {
  mapStateToProps,
  mapDispatchToProps
} from '../ToggleOrderContainer';

const previewsCode = 'ABC/1234';

test('Toggle Order Container', (t) => {
  t.test('Adds to order if selected item is not ordered', (t) => {
    const dispatchSpy = sinon.spy();
    const props = mapDispatchToProps(dispatchSpy);

    props.onItemSelected(previewsCode, false);

    t.equal(dispatchSpy.calledOnce, true);
    t.end();
  });

  t.test('Removes from order if selected item is ordered', (t) => {
    const dispatchSpy = sinon.spy();
    const props = mapDispatchToProps(dispatchSpy);

    props.onItemSelected(previewsCode, true);
    t.equal(dispatchSpy.calledOnce, true);
    t.ok(dispatchSpy.calledWith(removeFromOrder(previewsCode)));
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
