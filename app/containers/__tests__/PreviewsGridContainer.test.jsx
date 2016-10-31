/* eslint no-shadow: 0 */
import React from 'react';
import test from 'tape';
import { shallow } from 'enzyme';
import sinon from 'sinon';

import { mapDispatchToProps } from '../PreviewsGridContainer';

test('Previews Grid Container', (t) => {  
  t.test('Adds to order if selected item is not ordered', (t) => {
    const addToOrder = {
      type: 'ADD_TO_ORDER',
      orderItem: 'ABC/1234'
    };
    const dispatchSpy = sinon.spy();
    const props = mapDispatchToProps(dispatchSpy);
    
    props.onItemSelected('ABC/1234', false);
    t.equal(dispatchSpy.calledOnce, true);
    t.equal(dispatchSpy.calledWith(addToOrder), true);
    t.end();
  });

  t.test('Removes from order if selected item is ordered', (t) => {
    const removeFromOrder = {
      type: 'REMOVE_FROM_ORDER',
      orderItem: 'ABC/1234'
    };
    const dispatchSpy = sinon.spy();
    const props = mapDispatchToProps(dispatchSpy);
    
    props.onItemSelected('ABC/1234', true);
    t.equal(dispatchSpy.calledOnce, true);
    t.equal(dispatchSpy.calledWith(removeFromOrder), true);
    t.end();
  });
});
