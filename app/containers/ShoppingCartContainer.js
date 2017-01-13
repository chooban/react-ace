import { connect } from 'react-redux';
import ShoppingCart from '../components/ShoppingCart';
import { showOrder } from '../actions/';

const mapStateToProps = (state) => ({
  items: state.order.items,
  displayOrder: state.ui.showOrder
});

const mapDispatchToProps = (dispatch) => ({
  showCurrentOrder: () => dispatch(showOrder())
});

const ShoppingCartContainer = connect(
    mapStateToProps,
    mapDispatchToProps
)(ShoppingCart);

export default ShoppingCartContainer;
