/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import * as actions from '../../actions';

import {
  mapDispatchToProps
} from '../SearchContainer';

test('Dispatching searches', (t) => {
  t.test('Dispatches searches', (t) => {
    const dispatchSpy = sinon.spy();
    const actionSpy = sinon.spy(actions, 'updateSearch');

    const props = mapDispatchToProps(dispatchSpy);

    props.onSearchUpdate('foo');

    t.ok(dispatchSpy.calledOnce);
    t.ok(actionSpy.calledOnce);
    t.end();
  });
});
