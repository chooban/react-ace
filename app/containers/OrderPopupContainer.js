import { connect } from 'react-redux';

import { closeOrder, exportOrder } from '../actions/';
import OrderPopup from '../components/OrderPopup';

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
)(OrderPopup);

export default OrderPopupContainer;
