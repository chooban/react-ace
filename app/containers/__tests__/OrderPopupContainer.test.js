/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import {
  mapDispatchToProps,
  mapStateToProps,
  __RewireAPI__
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

  t.skip('Exporting the current order', (t) => {
    const orderToCsvSpy = sinon.stub().returns('A.N. Order');
    const fileDownloadSpy = sinon.spy();
    const dispatchSpy = sinon.spy();
    const getState = () => state;

    __RewireAPI__.__Rewire__('fileDownload', fileDownloadSpy);
    __RewireAPI__.__Rewire__('orderToCsv', orderToCsvSpy);
    const props = mapDispatchToProps(dispatchSpy);

    props.exportOrder()(dispatchSpy, getState);

    t.ok(orderToCsvSpy.calledOnce);
    t.ok(fileDownloadSpy.calledOnce);
    t.ok(fileDownloadSpy.calledWith('A.N. Order', 'order333.csv'));
    t.end();

    __RewireAPI__.__ResetDependency__('fileDownload');
    __RewireAPI__.__ResetDependency__('orderToCsv');
  });
});
