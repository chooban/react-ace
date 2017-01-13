import React from 'react';

const Modal = ({ isOpen, children }) => {
  if (!isOpen) {
    return null;
  }

  const modalStyle = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    zIndex: '9999',
    background: '#fff'
  };

  const backdropStyle = {
    position: 'absolute',
    width: '100%',
    height: '100%',
    top: '0px',
    left: '0px',
    zIndex: '9998',
    background: 'rgba(0, 0, 0, 0.3)'
  };

  return (
    <div>
      <div className="modal" style={modalStyle}>
        {children}
      </div>
      <div style={backdropStyle} />
    </div>
  );
};

Modal.propTypes = {
  isOpen: React.PropTypes.bool,
  children: React.PropTypes.instanceOf(Object)
};

export default Modal;
