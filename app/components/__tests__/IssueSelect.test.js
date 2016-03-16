import React from 'react'
import IssueSelect from '../IssueSelect.jsx'
import TestUtils from 'react-addons-test-utils'
import test from 'tape'
import Ramda from 'ramda'

function shallowRenderIssueSelect(issues) {
  const renderer = TestUtils.createRenderer()
  renderer.render(<IssueSelect issues={issues}/>)

  return renderer.getRenderOutput()
}

test('Issue Select component', (t) => {
  const issues = [
      100
    , 101
    , 102
  ]
  const result = shallowRenderIssueSelect(issues)

  t.test('It renders a label and options', (t) => {
    const isOption = Ramda.whereEq({ 'type': 'option' })
    const options = Ramda.filter(isOption, result.props.children[1].props.children)
    t.equal(result.props.children[0].props.children, "Pick an issue: ")
    t.equal(options.length, 3)
    t.end()
  })

})
