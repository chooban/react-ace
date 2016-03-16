import React from 'react'
import ReactDOM from 'react-dom'

export default React.createClass({
    displayName: "AddToOrder"
  , propTypes: {
      checked: React.PropTypes.boolean
    , onChange: React.PropTypes.function
  }
  , onChange(e) {
      var node = ReactDOM.findDOMNode(this)
      this.setState({
        checked: node.checked
      }, () => {
        this.props.onChange(node.checked)
      })
  }
  , getInitialState() {
      // Set initial checked status
      return {
        checked: this.props.checked
      }
  }
  , render() {
      return(
        <input
            type="checkbox"
            onChange={this.onChange}
            checked={this.state.checked} />
      )
  }
})
