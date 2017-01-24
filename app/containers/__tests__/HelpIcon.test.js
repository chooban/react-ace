/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import * as actions from '../../actions';

import { mapDispatchToProps } from '../HelpIcon';

test('Help Icon Container', (t) => {
  t.test('Call for help when clicked', (t) => {
    const dispatchSpy = sinon.spy();
    const actionSpy = sinon.spy(actions, 'showHelp');
    const props = mapDispatchToProps(dispatchSpy);

    props.display();

    t.equal(dispatchSpy.calledOnce, true);
    t.equal(actionSpy.calledOnce, true);
    t.end();
  });
});
