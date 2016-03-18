import {createClass} from 'react'
import {addToOrder, removeFromOrder} from '../actions/OrderActions'
import AddToOrder from './AddToOrder.jsx'
import OrderStore from '../stores/OrderStore'

export default createClass({
    displayName: "AddToOrderContainer"
  , propTypes: {
      lineItemDetails: React.PropTypes.object
    }
  , addItemToOrder() {
      addToOrder(
        this.props.lineItemDetails.issueNumber
      , this.props.lineItemDetails.id
      )
    }
  , removeItemFromOrder() {
      removeFromOrder(
        this.props.lineItemDetails.issueNumber
      , this.props.lineItemDetails.id
      )
  }
  , render() {
      const details = this.props.lineItemDetails
          , ordered = OrderStore.isOrdered(details.id)
          , onChange = (!ordered) ? this.addItemToOrder : this.removeItemFromOrder

      return(
        <AddToOrder
          onChange={onChange}
          checked={ordered}
        />
      )
    }
})
