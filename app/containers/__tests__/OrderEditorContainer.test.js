/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import {
  mapDispatchToProps,
  mapStateToProps
} from '../OrderEditorContainer';
import { removeFromOrder } from '../../actions';

test('Order editor container', (t) => {
  t.test('Provides a callback for removing items', (t) => {
    const code = '332/0001';
    const dispatchSpy = sinon.spy();
    const props = mapDispatchToProps(dispatchSpy);

    props.onRemoveItem(code);

    t.ok(dispatchSpy.calledOnce);
    t.ok(dispatchSpy.calledWith(removeFromOrder(code)));
    t.end();
  });

  t.test('Orders order items', (t) => {
    const items = [
      { publisher: 'Marvel', title: 'Spider-Man' },
      { publisher: 'Image', title: 'Spawn' },
      { publisher: 'Image', title: 'Wildcats' },
      { publisher: 'Marvel', title: 'Avengers' }
    ];

    const state = mapStateToProps({
      order: {
        items
      }
    });

    t.deepEqual(state.items, [
      { publisher: 'Image', title: 'Spawn' },
      { publisher: 'Image', title: 'Wildcats' },
      { publisher: 'Marvel', title: 'Avengers' },
      { publisher: 'Marvel', title: 'Spider-Man' }
    ]);
    t.end();
  });
});
