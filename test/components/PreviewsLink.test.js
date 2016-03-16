import React from 'react'
import PreviewsLink from '../../app/components/PreviewsLink.jsx'
import TestUtils from 'react-addons-test-utils'
import test from 'tape'
import Ramda from 'ramda'


test('Previews Link component', (t) => {

  fixtures.forEach((v) => {
    t.test('Testing previews link for ' + v.previewsCode, (t) => {
      const result = shallowRender(v.previewsCode)
      t.equal(result.props.href, v.url, "Should generate Previews World link")
      t.equal(result.props.children, v.previewsCode, "Should display Previews Code")
      t.end()
    })
  })
})

function shallowRender(previewsCode) {
  const renderer = TestUtils.createRenderer()
  renderer.render(<PreviewsLink previewsCode={previewsCode}/>)

  return renderer.getRenderOutput()
}

const fixtures = [
  {
      previewsCode:'330/0001'
    , url: previewsUrl('MAR160001')
  }
, {
      previewsCode:'331/0001'
    , url: previewsUrl('APR160001')
  }
, {
      previewsCode:'332/0001'
    , url: previewsUrl('MAY160001')
  }
, {
      previewsCode:'333/0001'
    , url: previewsUrl('JUN160001')
  }
, {
      previewsCode:'334/0001'
    , url: previewsUrl('JUL160001')
  }
, {
      previewsCode:'335/0001'
    , url: previewsUrl('AUG160001')
  }
, {
      previewsCode:'336/0001'
    , url: previewsUrl('SEP160001')
  }
, {
      previewsCode:'337/0001'
    , url: previewsUrl('OCT160001')
  }
, {
      previewsCode:'338/0001'
    , url: previewsUrl('NOV160001')
  }
, {
      previewsCode:'339/0001'
    , url: previewsUrl('DEC160001')
  }
, {
      previewsCode:'340/0001'
    , url: previewsUrl('JAN170001')
  }
, {
      previewsCode:'341/0001'
    , url: previewsUrl('FEB170001')
  }
]

function previewsUrl(pc) {
  return `http://www.previewsworld.com/Catalog/${pc}`
}
