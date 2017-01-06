import React from 'react';

const OrderSummary = ({ items, showCurrentOrder }) => (
  <div className="ordersummary">
    <i // eslint-disable-line
      className={`fa fa-shopping-cart fa-2x ${(items.length > 0 ? 'hasitems' : '')}`}
      onClick={showCurrentOrder}
    />
  </div>
);

OrderSummary.propTypes = {
  items: React.PropTypes.instanceOf(Array),
  showCurrentOrder: React.PropTypes.func
};

export default OrderSummary;
