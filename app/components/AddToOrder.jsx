import React from 'react'

export default React.createClass({
    displayName: "AddToOrder"
  , propTypes: {
      previewsCode: React.PropTypes.string
  }
  , render() {
      return(
        <input type="checkbox" value="{previewsCode}"></input>
      )
  }
})
