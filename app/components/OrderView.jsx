import React from 'react';

const OrderView = ({ items, exportCurrentOrder, showCurrentOrder }) => (
  <div>
    Ordered items: {items.length} <br />
    <input
      type="button"
      value="Show"
      onClick={showCurrentOrder}
      disabled={items.length === 0}
    />
    <input
      type="button"
      value="Export"
      onClick={exportCurrentOrder}
      disabled={items.length === 0}
    />
  </div>
);

OrderView.propTypes = {
  items: React.PropTypes.instanceOf(Array),
  exportCurrentOrder: React.PropTypes.func,
  showCurrentOrder: React.PropTypes.func
};

export default OrderView;
