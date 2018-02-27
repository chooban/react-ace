/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import { mapDispatchToProps } from '../AddNewSavedSearchContainer';
import { addSavedSearch } from '../../actions';

test('Add new saved search container', (t) => {
  t.test('Adding a new search dispatches action', (t) => {
    const dispatchSpy = sinon.spy();
    const props = mapDispatchToProps(dispatchSpy);

    props.onAdd('foo');

    t.ok(dispatchSpy.calledOnce);
    t.ok(dispatchSpy.calledWith(addSavedSearch('foo')));
    t.end();
  });
});
