/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import { updateSearch } from '../../actions';

import {
  mapDispatchToProps,
  mapStateToProps
} from '../SearchContainer';

test('Dispatching searches', (t) => {
  t.test('Dispatches searches', (t) => {
    const dispatchSpy = sinon.spy();
    const action = updateSearch('foo');

    const props = mapDispatchToProps(dispatchSpy);

    props.onSearchUpdate('foo');

    t.ok(dispatchSpy.calledOnce);
    t.ok(dispatchSpy.calledWith(action));
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
