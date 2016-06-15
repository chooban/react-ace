import React from 'react';
import { connect } from 'react-redux';

const OrderView = ({ items }) => (
  <p>Ordered items: {items.size}</p>
);

OrderView.propTypes = {
  items: React.PropTypes.instanceOf(Set)
};

const stateToProps = (state) => (
  { items: state.order.items }
);

const OrderViewComponent = connect(stateToProps)(OrderView);

export default OrderViewComponent;
