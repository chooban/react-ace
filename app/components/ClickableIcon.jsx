import React from 'react';

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
  onClick: React.PropTypes.func,
  className: React.PropTypes.string,
  iconName: React.PropTypes.string
};

ClickableIcon.defaultProps = {
  onClick: () => ({}),
  className: '',
  iconName: ''
};

export default ClickableIcon;
