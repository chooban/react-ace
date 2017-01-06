import React from 'react';

const ToggleOrderComponent = ({ previewsCode, ordered, onItemSelected }) => (
  <div
    className="toggle-order"
  >
    <i //eslint-disable-line
      className={ordered
        ? 'fa fa-check-square-o'
        : 'fa fa-square-o'
      }
      onClick={() => onItemSelected(previewsCode, ordered)}
    />
  </div>
);

ToggleOrderComponent.propTypes = {
  previewsCode: React.PropTypes.string,
  ordered: React.PropTypes.bool,
  onItemSelected: React.PropTypes.func
};

export default ToggleOrderComponent;
