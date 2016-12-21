import React from 'react';

const OrderView = ({ items, exportOrder }) => (
  <div>
    Ordered items: {items.size} <br />
    <input
      type="button"
      value="Export"
      onClick={exportOrder}
      disabled={items.size === 0}
    />
  </div>
);

OrderView.propTypes = {
  items: React.PropTypes.instanceOf(Set),
  exportOrder: React.PropTypes.func
};

export default OrderView;
