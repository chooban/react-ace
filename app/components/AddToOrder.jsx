import React from 'react'
import ReactDOM from 'react-dom'

export default React.createClass({
    displayName: "AddToOrder"
  , propTypes: {
      checked: React.PropTypes.bool
    , onChange: React.PropTypes.func
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
      return {
        checked: this.props.checked
      }
  }
  , render() {
      return(
        <input
            type="checkbox"
            onChange={this.onChange}
            checked={this.state.checked}
        />
      )
  }
})
