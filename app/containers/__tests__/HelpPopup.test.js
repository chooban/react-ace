/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import {
  mapStateToProps,
  mapDispatchToProps
} from '../HelpPopup';

import { closeHelp } from '../../actions';

test('The help popup', (t) => {
  t.test('Display property determined by state: false', (t) => {
    const state = {
      ui: {
        showHelp: false
      }
    };

    const props = mapStateToProps(state);
    t.notOk(props.display);
    t.end();
  });

  t.test('Display property determined by state: true', (t) => {
    const state = {
      ui: {
        showHelp: true
      }
    };

    const props = mapStateToProps(state);
    t.ok(props.display);
    t.end();
  });

  t.test('Dispatches closeHelp even on callback', (t) => {
    const dispatchSpy = sinon.spy();
    const props = mapDispatchToProps(dispatchSpy);

    props.close();

    t.ok(dispatchSpy.calledOnce);
    t.ok(dispatchSpy.calledWith(closeHelp()));
    t.end();
  });
});
