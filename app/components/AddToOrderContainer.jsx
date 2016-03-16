import React from 'react'
import {addToOrder, removeFromOrder} from '../actions/OrderActions'
import AddToOrder from './AddToOrder.jsx'
import OrderStore from '../stores/OrderStore'

export default React.createClass({
    displayName: "AddToOrderContainer"
  , propTypes: {
      lineItemDetails: React.PropTypes.object
    }
  , onChange(isChecked) {
      const details = this.props.lineItemDetails
      return (isChecked)
              ? addToOrder(details.issueNumber, details.id)
              : removeFromOrder(details.issueNumber, details.id)
  }
  , render() {
      const details = this.props.lineItemDetails
      return(
        <AddToOrder
          onChange={this.onChange}
          checked={OrderStore.isOrdered(details.id)}
        />
      )
    }
})
