import React from 'react';

const ToggleOrderComponent = ({ previewsCode, ordered, onItemSelected }) => (
  <div
    className="toggle-order"
  >
    <i //eslint-disable-line
      className="material-icons"
      onClick={() => onItemSelected(previewsCode, ordered)}
    >
      {ordered
        ? 'check_box'
        : 'check_box_outline_blank'
      }
    </i>
  </div>
);

ToggleOrderComponent.propTypes = {
  previewsCode: React.PropTypes.string,
  ordered: React.PropTypes.bool,
  onItemSelected: React.PropTypes.func
};

export default ToggleOrderComponent;
