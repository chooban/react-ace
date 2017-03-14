import React from 'react';
import { connect } from 'react-redux';

import OrderEditor from '../containers/OrderEditorContainer';
import { closeOrder, exportOrder } from '../actions/';
import Modal from '../components/Modal';

const OrderPopupComponent = ({ display, onExport, onClose, hasOrder }) => (
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
        className="btn-flat"
        onClick={onClose}
      >
        Cancel
      </a>
      <a
        tabIndex="-1"
        className="btn-flat"
        onClick={onExport}
        disabled={!hasOrder}
      >
        Export
      </a>
    </div>
  </Modal>
);

OrderPopupComponent.propTypes = {
  display: React.PropTypes.bool.isRequired,
  onExport: React.PropTypes.func.isRequired,
  onClose: React.PropTypes.func.isRequired,
  hasOrder: React.PropTypes.bool.isRequired
};

export const mapDispatchToProps = (dispatch) => ({
  onClose: () => dispatch(closeOrder()),
  onExport: () => dispatch(exportOrder())
});

export const mapStateToProps = (state) => ({
  hasOrder: !!state.order.items.length,
  display: state.ui.showOrder
});

const OrderPopupContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(OrderPopupComponent);

export default OrderPopupContainer;
