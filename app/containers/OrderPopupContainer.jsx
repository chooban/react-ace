import React from 'react';
import { connect } from 'react-redux';

import OrderEditor from '../containers/OrderEditorContainer';
import { closeOrder } from '../actions/';
import Modal from '../components/Modal';
import fileDownload from '../utils/FileDownload';
import orderToCsv from '../utils/OrderToCsv';

const OrderPopupComponent = ({ display, exportOrder, close }) => (
  <Modal isOpen={display} onClose={close}>
    <div className="ordermodal">
      <div className="header">
          Order Contents
        </div>
      <div className="contents">
        <OrderEditor />
      </div>
      <div className="footer">
        <a
          tabIndex="-2"
          className="btn-flat"
          onClick={close}
        >
          Cancel
        </a>
        <a
          tabIndex="-1"
          className="btn-flat"
          onClick={exportOrder}
        >
          Export
        </a>
      </div>
    </div>
  </Modal>
);

OrderPopupComponent.propTypes = {
  display: React.PropTypes.bool,
  exportOrder: React.PropTypes.func,
  close: React.PropTypes.func
};

const mapStateToProps = (state) => ({
  display: state.ui.showOrder
});

function exportCurrentOrder() {
  return (dispatch, getStore) => {
    const store = getStore();
    fileDownload(orderToCsv(store.order.items), `order${store.order.issue}.csv`);
  };
}

const OrderPopupContainer = connect(
  mapStateToProps,
  {
    exportOrder: exportCurrentOrder,
    close: () => (dispatch) => dispatch(closeOrder())
  }
)(OrderPopupComponent);

export default OrderPopupContainer;
