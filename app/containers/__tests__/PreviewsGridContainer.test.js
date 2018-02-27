/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import { mapDispatchToProps } from '../PreviewsGridContainer';
import {
  nextPage,
  previousPage,
  showPreview
} from '../../actions/';

test('Previews Grid', (t) => {
  t.test('Going to the next page', (t) => {
    const dispatchSpy = sinon.spy();
    const props = mapDispatchToProps(dispatchSpy);
    props.nextPage();

    t.ok(dispatchSpy.calledOnce);
    t.ok(dispatchSpy.calledWith(nextPage()));
    t.end();
  });

  t.test('Going to the previous page', (t) => {
    const dispatchSpy = sinon.spy();
    const props = mapDispatchToProps(dispatchSpy);
    props.previousPage();

    t.ok(dispatchSpy.calledOnce);
    t.ok(dispatchSpy.calledWith(previousPage()));
    t.end();
  });

  t.test('Showing a preview', (t) => {
    const dispatchSpy = sinon.spy();
    const props = mapDispatchToProps(dispatchSpy);
    props.showPreview('foo');

    t.ok(dispatchSpy.calledOnce);
    t.ok(dispatchSpy.calledWith(showPreview('foo')));
    t.end();
  });
});
