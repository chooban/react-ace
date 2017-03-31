import React from 'react';

import OrderEditor from '../containers/OrderEditorContainer';
import Modal from './Modal';

const OrderPopup = ({ display, onExport, onClose, hasOrder }) => (
  <Modal isOpen={display}>
    <div className="header">
      Order Contents
    </div>
    <div className="contents">
      { hasOrder
        ? <OrderEditor />
        : <p>Your cart is empty</p>
      }
    </div>
    <div className="footer">
      <a
        tabIndex="-2"
        className="btn blue-grey lighten-3"
        onClick={onClose}
      >
        Cancel
      </a>
      <a
        tabIndex="-1"
        className="btn"
        onClick={onExport}
        disabled={!hasOrder}
      >
        Export
      </a>
    </div>
  </Modal>
);

OrderPopup.propTypes = {
  display: React.PropTypes.bool.isRequired,
  onExport: React.PropTypes.func.isRequired,
  onClose: React.PropTypes.func.isRequired,
  hasOrder: React.PropTypes.bool.isRequired
};

export default OrderPopup;
