import { connect } from 'react-redux';
import OrderSummary from '../components/OrderSummary';
import { showOrder } from '../actions/';

const mapStateToProps = (state) => ({
  items: state.order.items,
  displayOrder: state.ui.showOrder
});

const mapDispatchToProps = (dispatch) => ({
  showCurrentOrder: () => dispatch(showOrder())
});

const OrderViewContainer = connect(
    mapStateToProps,
    mapDispatchToProps
)(OrderSummary);

export default OrderViewContainer;
