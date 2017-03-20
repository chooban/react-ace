/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import { clearOrder } from '../../actions';
import middleware from '../RemoveOldOrderObserver';

test.test('Removing the old order', (t) => {
  t.test('Does not remove if issue number matches', (t) => {
    const downloadedFile = {
      file: 'ecmail333',
      data: []
    };
    const currentOrder = {
      issue: 'ecmail333',
      items: []
    };

    const fakeStore = {
      getState: () => ({ order: currentOrder }),
      dispatch: sinon.spy()
    };
    const fakeNext = sinon.spy();
    const action = {
      type: 'RECEIVED_ISSUE_DATA',
      payload: downloadedFile
    };

    middleware(fakeStore)(fakeNext)(action);
    t.ok(fakeStore.dispatch.notCalled);
    t.end();
  });

  t.test('Removes if issue number does not match', (t) => {
    const downloadedFile = {
      file: 'ecmail334',
      data: []
    };
    const currentOrder = {
      issue: 'ecmail333',
      items: []
    };

    const fakeStore = {
      getState: () => ({ order: currentOrder }),
      dispatch: sinon.spy()
    };
    const fakeNext = sinon.spy();
    const action = {
      type: 'RECEIVED_ISSUE_DATA',
      payload: downloadedFile
    };

    middleware(fakeStore)(fakeNext)(action);
    t.ok(fakeStore.dispatch.withArgs(clearOrder()).calledOnce);
    t.end();
  });
});
