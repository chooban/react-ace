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
  , onChange(e) {
      var node = ReactDOM.findDOMNode(this)
      return (node.checked)
              ? addToOrder(this.props.issueNumber, this.props.previewsCode)
              : removeFromOrder(this.props.issueNumber, this.props.previewsCode)
  }
  , render() {
      return(
        <input type="checkbox" value="{previewsCode}" onChange={this.onChange}></input>
      )
  }
})
