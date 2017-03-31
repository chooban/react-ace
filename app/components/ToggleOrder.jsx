import React from 'react';

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
  previewsCode: React.PropTypes.string.isRequired,
  ordered: React.PropTypes.bool,
  onItemSelected: React.PropTypes.func.isRequired,
  type: React.PropTypes.string
};

ToggleOrderComponent.defaultProps = {
  type: 'checkbox',
  ordered: false
};

export default ToggleOrderComponent;
