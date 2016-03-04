import React from 'react'

export default React.createClass({
    displayName: "PreviewsGrid"
  , propTypes : {
      selectedIssue: React.PropTypes.number
    }
  , render() {
    const msg = (this.props.selectedIssue)
                  ? "Selected issue is " + this.props.selectedIssue
                  : "No issue currently selected"

    return(<div>{msg}</div>)
  }
})
