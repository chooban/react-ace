import React from 'react';
import PropTypes from 'prop-types';

const ToggleOrderComponent = ({ previewsCode, ordered, onItemSelected, type }) => {
  if (type === 'checkbox') {
    return (
      <i //eslint-disable-line
        className={`material-icons toggle-order ${ordered ? 'ordered' : ''}`}
        onClick={() => onItemSelected(previewsCode, ordered)}
      >
        {ordered
          ? 'check_box'
          : 'check_box_outline_blank'
        }
      </i>
    );
  }

  return (
    <a
      tabIndex="-1"
      className="btn"
      onClick={() => {
        onItemSelected(previewsCode, ordered);
      }}
    >
      { ordered
        ? 'Remove From Order'
        : 'Add To Order'
      }
    </a>
  );
};

ToggleOrderComponent.propTypes = {
  previewsCode: PropTypes.string.isRequired,
  ordered: PropTypes.bool,
  onItemSelected: PropTypes.func.isRequired,
  type: PropTypes.string
};

ToggleOrderComponent.defaultProps = {
  type: 'checkbox',
  ordered: false
};

export default ToggleOrderComponent;
