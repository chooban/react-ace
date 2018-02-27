/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import middleware, { __RewireAPI__ } from '../ExportOrderObserver';

test('Order exporting middleware', (t) => {
  t.test('should pass the intercepted action to next', (t) => {
    const fakeStore = {};
    const fakeNext = sinon.spy();

    const action = {
      type: 'CLOSE_SAVED_SEARCHES',
      payload: null
    };

    middleware(fakeStore)(fakeNext)(action);

    t.ok(fakeNext.withArgs(action).calledOnce);
    t.end();
  });

  t.test('should export on the right action', (t) => {
    const fakeStore = {
      getState: () => ({
        order: {
          issue: '333',
          items: ['a', 'b', 'c']
        }
      })
    };
    const fakeNext = sinon.spy();
    const orderToCsvSpy = sinon.spy();
    const fileDownloadSpy = sinon.spy();

    __RewireAPI__.__Rewire__('orderToCsv', orderToCsvSpy);
    __RewireAPI__.__Rewire__('fileDownload', fileDownloadSpy);

    const action = {
      type: 'EXPORT_ORDER',
      payload: null
    };

    middleware(fakeStore)(fakeNext)(action);

    t.ok(fakeNext.withArgs(action).calledOnce);
    t.ok(orderToCsvSpy.withArgs(['a', 'b', 'c']).calledOnce);
    t.ok(fileDownloadSpy.calledOnce);
    t.end();

    __RewireAPI__.__ResetDependency__('orderToCsv');
    __RewireAPI__.__ResetDependency__('fileDownload');
  });
});
