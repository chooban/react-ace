import React from 'react';
import AddToOrder from '../AddToOrder.jsx';
import test from 'tape';
import { shallow } from 'enzyme';
import sinon from 'sinon';

test('Add To Order component', (t) => {

  t.test('Renders a checked component', (t) => {
    const changeSpy = sinon.spy();

    const result = shallowRender({
      onChange: changeSpy, checked: true,
    });
    t.equal(result.node.props.checked, true);
    t.equal(changeSpy.called, false);
    t.end();
  });

  t.test('Renders an unchecked component', (t) => {
    const changeSpy = sinon.spy();
    const result = shallowRender({
      onChange: changeSpy, checked: false,
    });

    t.equal(result.node.props.checked, false);
    t.equal(changeSpy.called, false);
    t.end();
  })

  ;[true, false].forEach((v) => {
    t.test('Invokes the passed function on change events', (t) => {
      const changeSpy = sinon.spy();
      const wrapper = shallow(<AddToOrder
              onChange={changeSpy}
              checked={false}
            />);

      wrapper.find('input').simulate('change', { target: { checked: v } });

      t.equal(changeSpy.calledOnce, true, 'Callback invoked');
      t.equal(changeSpy.calledWith(v), true, 'Callback invoked with checked status');
      t.end();
    });

  });
});

function shallowRender(props) {
  return shallow(<AddToOrder
      onChange={props.onChange}
      checked={props.checked}
    />
  );
}
