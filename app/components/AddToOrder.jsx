import React from 'react'
import {addToOrder, removeFromOrder} from '../actions/OrderActions'
import OrderStore from '../stores/OrderStore'
import ReactDOM from 'react-dom'

export default React.createClass({
    displayName: "AddToOrder"
  , propTypes: {
      previewsCode: React.PropTypes.string
    , issueNumber: React.PropTypes.string
  }
  , getInitialState() {
      return {
        checked: false
      }
  }
  , onChange(e) {
      var node = ReactDOM.findDOMNode(this)
      this.setState({
        checked: node.checked
      })
      return (node.checked)
              ? addToOrder(this.props.issueNumber, this.props.previewsCode)
              : removeFromOrder(this.props.issueNumber, this.props.previewsCode)
  }
  , render() {
      return(
        <input type="checkbox" value="{previewsCode}" onChange={this.onChange} checked={this.state.checked}></input>
      )
  }
})
