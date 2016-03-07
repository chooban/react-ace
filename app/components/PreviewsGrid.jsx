import React from 'react'

export default React.createClass({
    displayName: 'PreviewsGrid'
  , propTypes: {
      issueNumber: React.PropTypes.number
  }
  , render() {
      return(<p>This is the grid for {this.props.issueNumber}</p>)
  }
})
