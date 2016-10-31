/* eslint no-shadow: 0 */
import React from 'react';
import test from 'tape';
import { shallow } from 'enzyme';
import sinon from 'sinon';

import { ToggleOrderComponent } from '../ToggleOrderContainer';

function render(ordered, onItemSelected, previewsCode) {
  return shallow(
    <ToggleOrderComponent
      ordered={ordered}
      onItemSelected={onItemSelected}
      previewsCode={previewsCode}
    />
  );
}

test('Toggle Order', (t) => {
  t.test('Class for ordered items', (t) => {
    const result = render(true, null, '');
    t.equal(result.find('.toggleOrder').length, 1);
    t.equal(result.find('button').hasClass('ordered'), true);
    t.end();
  });

  t.test('Class for unordered items', (t) => {
    const result = render(false, null, '');
    t.equal(result.find('button').hasClass('notordered'), true);
    t.end();
  });

  t.test('Clicking invokes callback (ordered)', (t) => {
    const onClick = sinon.spy();
    const previewsCode = 'ABC/1234';
    const result = render(true, onClick, previewsCode);
    result.find('button').simulate('click');

    t.equal(onClick.calledOnce, true);
    t.equal(onClick.calledWith(previewsCode, true), true);
    t.end();
  });

  t.test('Clicking invokes callback (not ordered)', (t) => {
    const onClick = sinon.spy();
    const previewsCode = 'ABC/1234';
    const result = render(false, onClick, previewsCode);
    result.find('button').simulate('click');

    t.equal(onClick.calledOnce, true);
    t.equal(onClick.calledWith(previewsCode, false), true);
    t.end();
  });
});
