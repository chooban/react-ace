/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import {
  mapDispatchToProps,
  mapStateToProps
} from '../OrderPopupContainer';

import { closeOrder, exportOrder } from '../../actions';

test('Order popup', (t) => {
  const state = {
    order: {
      issue: 333,
      items: ['a', 'b', 'c']
    },
    ui: {
      showOrder: true
    }
  };

  t.test('has a display prop', (t) => {
    const props = mapStateToProps(state);

    t.ok(props.display);
    t.ok(props.hasOrder);
    t.end();
  });

  t.test('The close function dispatches the close action', (t) => {
    const dispatchSpy = sinon.spy();
    const props = mapDispatchToProps(dispatchSpy);

    props.onClose();

    t.ok(dispatchSpy.calledOnce);
    t.ok(dispatchSpy.calledWith(closeOrder()));
    t.end();
  });

  t.test('The export function dispatches the exportOrder action', (t) => {
    const dispatchSpy = sinon.spy();
    const props = mapDispatchToProps(dispatchSpy);

    props.onExport();

    t.ok(dispatchSpy.calledOnce);
    t.ok(dispatchSpy.calledWith(exportOrder()));
    t.end();
  });
});
