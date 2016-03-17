import React from 'react'
import AddToOrder from '../AddToOrder.jsx'
import TestUtils from 'react-addons-test-utils'
import test from 'tape'
import sinon from 'sinon'

test.only('Add To Order component', (t) => {

  t.test('Renders a checked component', (t) => {
    var result = shallowRender({
      onChange: sinon.spy()
    , checked: true
    })
    t.equal(result.props.checked, true)
    t.notOk(result.props.onChange.called)
    t.end()
  })

  t.test('Renders an unchecked component', (t) => {
    var result = shallowRender({
      onChange: sinon.spy()
    , checked: false
    })
    t.equal(result.props.checked, false)
    t.notOk(result.props.onChange.called)
    t.end()
  })

  t.test('Invokes the passed function on change events', (t) => {
    var result = shallowRender({
      onChange: sinon.spy()
    , checked: false
    })
    console.log(result)
    // TestUtils.Simulate.click()
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
