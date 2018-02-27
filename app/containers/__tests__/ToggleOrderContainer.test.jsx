/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import { removeFromOrder } from '../../actions';
import { mapDispatchToProps } from '../ToggleOrderContainer';

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
});
