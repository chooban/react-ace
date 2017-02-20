/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import * as actions from '../../actions';

import {
  mapDispatchToProps,
  mapStateToProps
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

  t.test('Extract search term from store', (t) => {
    t.deepEqual(mapStateToProps({
      gridConfig: {
        searchTerm: 'marvel'
      }
    }), {
      searchValue: 'marvel'
    });
    t.end();
  });
});
