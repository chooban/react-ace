import React from 'react';

const OrderSummary = ({ items, showCurrentOrder }) => (
  <div className="ordersummary">
    <i
      className={`material-icons ${(items.length > 0 ? 'hasitems' : '')}`}
      onClick={showCurrentOrder}
    >
    shopping_cart
    </i>
  </div>
);

OrderSummary.propTypes = {
  items: React.PropTypes.instanceOf(Array),
  showCurrentOrder: React.PropTypes.func
};

export default OrderSummary;
