import React from 'react';
import ReactDOM from 'react-dom';

const AddToOrder = ({ checked, onChange }) => (
  <input
    type="checkbox"
    checked={checked}
    onChange={(e) => onChange(e.target.checked)}/>
);

export default AddToOrder;
