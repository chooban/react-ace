import React from 'react';

const ShoppingCart = ({ items, showCurrentOrder }) => (
  <div className="ordersummary">
    <i
      className={`material-icons ${(items.length > 0 ? 'hasitems' : '')}`}
      onClick={showCurrentOrder}
    >
    shopping_cart
    </i>
  </div>
);

ShoppingCart.propTypes = {
  items: React.PropTypes.instanceOf(Array),
  showCurrentOrder: React.PropTypes.func
};

export default ShoppingCart;
