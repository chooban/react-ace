/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import {
  mapStateToProps,
  mapDispatchToProps
} from '../PreviewsItemViewContainer';

import { closePreview } from '../../actions/';

test('Previews Item View', (t) => {
  t.test('Extracts fields from store', (t) => {
    const state = {
      ui: {
        showItemPreview: true,
        itemPreview: '333/0001'
      }
    };

    const props = mapStateToProps(state);

    t.ok(props.display);
    t.equal('333/0001', props.previewsCode);
    t.end();
  });

  t.test('Dispatches the close action', (t) => {
    const dispatchSpy = sinon.spy();
    const props = mapDispatchToProps(dispatchSpy);
    props.close();

    t.ok(dispatchSpy.calledOnce);
    t.ok(dispatchSpy.calledWith(closePreview()));
    t.end();
  });
});
