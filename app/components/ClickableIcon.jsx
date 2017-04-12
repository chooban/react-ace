import React from 'react';
import PropTypes from 'prop-types';

const ClickableIcon = ({ className, onClick, iconName }) => (
  <div
    className={className}
  >
    <i
      className="material-icons click"
      onClick={onClick}
    >
      {iconName}
    </i>
  </div>
);

ClickableIcon.propTypes = {
  onClick: PropTypes.func,
  className: PropTypes.string,
  iconName: PropTypes.string
};

ClickableIcon.defaultProps = {
  onClick: () => ({}),
  className: '',
  iconName: ''
};

export default ClickableIcon;
