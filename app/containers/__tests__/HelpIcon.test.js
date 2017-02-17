/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import * as actions from '../../actions';

import {
  mapStateToProps,
  mapDispatchToProps
} from '../HelpIcon';

test('Help Icon Container', (t) => {
  t.test('Call for help when clicked', (t) => {
    const dispatchSpy = sinon.spy();
    const actionSpy = sinon.spy(actions, 'showHelp');
    const props = mapDispatchToProps(dispatchSpy);

    props.onClick();

    t.equal(dispatchSpy.calledOnce, true);
    t.equal(actionSpy.calledOnce, true);
    t.end();
  });

  t.test('Static props', (t) => {
    const props = mapStateToProps();

    t.equals(props.className, 'showhelp');
    t.equals(props.iconName, 'help');

    t.end();
  });
});
