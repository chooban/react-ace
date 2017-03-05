/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import {
  mapStateToProps,
  mapDispatchToProps
} from '../HelpIcon';

import { showHelp } from '../../actions';

test('Help Icon Container', (t) => {
  t.test('Call for help when clicked', (t) => {
    const dispatchSpy = sinon.spy();
    const props = mapDispatchToProps(dispatchSpy);

    props.onClick();

    t.equal(dispatchSpy.calledOnce, true);
    t.ok(dispatchSpy.calledWith(showHelp()));
    t.end();
  });

  t.test('Static props', (t) => {
    const props = mapStateToProps();

    t.equals(props.className, 'showhelp');
    t.equals(props.iconName, 'help');

    t.end();
  });
});
