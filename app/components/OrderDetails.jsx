import React from 'react';
import OrderStore from '../stores/OrderStore';

export default React.createClass({
  displayName: 'OrderDetails',

  getInitialState() {
    return {
      totalCost: 0,
      numberOfItems: 0,
    };
  },

  componentWillMount() {
    OrderStore.addChangeListener(this.onStoreChange);
  },

  onStoreChange() {
    var metadata = OrderStore.getCurrentOrderMetadata();
    console.log(metadata);
    this.setState({
      numberOfItems: metadata,
    });
  },

  render() {
    return (
      <div className="orderDetails">
        <strong>Items: </strong> {this.state.numberOfItems}
      </div>
    );
  },
});
