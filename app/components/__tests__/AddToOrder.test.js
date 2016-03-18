import React from 'react'
import AddToOrder from '../AddToOrder.jsx'
import TestUtils from 'react-addons-test-utils'
import test from 'tape'
import {shallow} from 'enzyme'
import sinon from 'sinon'

test('Add To Order component', (t) => {

  t.test('Renders a checked component', (t) => {
    const result = shallowRender({
      onChange: sinon.spy()
    , checked: true
    })

    t.equal(result.props.checked, true)
    t.notOk(result.props.onChange.called)
    t.end()
  })

  t.test('Renders an unchecked component', (t) => {
    const result = shallowRender({
            onChange: sinon.spy()
          , checked: false
        })

    t.equal(result.props.checked, false)
    t.equal(result.props.onChange.called, undefined)
    t.end()
  })

  ;[true, false].forEach((v) => {
    t.test('Invokes the passed function on change events', (t) => {
      const onChangeEvent = sinon.spy()
      const wrapper = shallow(<AddToOrder
              onChange={onChangeEvent}
              checked={false}
            />)

      wrapper.find('input').simulate('change', { target: { checked: v } })

      t.equal(onChangeEvent.calledOnce, true, "Callback invoked")
      t.equal(onChangeEvent.calledWith(v), true, "Callback invoked with checked status")
      t.end()
    })

  })
})

function shallowRender(props) {
  const renderer = TestUtils.createRenderer()
  renderer.render(<AddToOrder
      onChange={props.onChange}
      checked={props.checked}
    />
  )
  return renderer.getRenderOutput()
}
