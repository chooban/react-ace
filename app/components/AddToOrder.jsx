import React from 'react';

const AddToOrder = ({ checked, onChange }) => (
  <input
    type="checkbox"
    checked={checked}
    onChange={(e) => onChange(e.target.checked)}
  />
);

AddToOrder.propTypes = {
  checked: React.PropTypes.boolean,
  onChange: React.PropTypes.function
};

export default AddToOrder;
