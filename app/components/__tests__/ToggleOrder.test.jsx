/* eslint no-shadow: 0 */
import React from 'react';
import test from 'tape';
import sinon from 'sinon';
import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-15';

import ToggleOrderComponent from '../ToggleOrder';

function render(ordered, onItemSelected, previewsCode) {
  return shallow(<ToggleOrderComponent
    ordered={ordered}
    onItemSelected={onItemSelected}
    previewsCode={previewsCode}
  />);
}
configure({ adapter: new Adapter() });

test('Toggle Order', (t) => {
  t.test('Clicking invokes callback (ordered)', (t) => {
    const onClick = sinon.spy();
    const previewsCode = 'ABC/1234';
    const result = render(true, onClick, previewsCode);
    result.find('i').simulate('click');

    t.equal(onClick.calledOnce, true);
    t.equal(onClick.calledWith(previewsCode, true), true);
    t.end();
  });

  t.test('Clicking invokes callback (not ordered)', (t) => {
    const onClick = sinon.spy();
    const previewsCode = 'ABC/1234';
    const result = render(false, onClick, previewsCode);
    result.find('i').simulate('click');

    t.equal(onClick.calledOnce, true);
    t.equal(onClick.calledWith(previewsCode, false), true);
    t.end();
  });
});
