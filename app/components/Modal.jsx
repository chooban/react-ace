import React from 'react';
import PropTypes from 'prop-types';

const Modal = ({
  isOpen, children, height, width
}) => {
  if (!isOpen) {
    return null;
  }

  const modalStyle = {
    width,
    height
  };

  const backdropStyle = {
    position: 'fixed',
    width: '100%',
    height: '100%',
    top: '0px',
    left: '0px',
    zIndex: '9998',
    background: 'rgba(0, 0, 0, 0.3)'
  };

  return (
    <div className="modalcontainer">
      <div className="modal" style={modalStyle}>
        {children}
      </div>
      <div style={backdropStyle} />
    </div>
  );
};

Modal.propTypes = {
  isOpen: PropTypes.bool,
  children: PropTypes.instanceOf(Object).isRequired,
  width: PropTypes.string,
  height: PropTypes.string
};

Modal.defaultProps = {
  isOpen: false,
  height: 'auto',
  width: '700px'
};

export default Modal;
