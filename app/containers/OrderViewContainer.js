import { connect } from 'react-redux';
import OrderView from '../components/OrderView';
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
)(OrderView);

export default OrderViewContainer;
