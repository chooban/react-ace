import React from 'react';

const ToggleOrderComponent = ({ previewsCode, ordered, onItemSelected, type }) => {
  if (type === 'checkbox') {
    return (
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
  }

  return (
    <a
      tabIndex="-1"
      className="btn-flat"
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
