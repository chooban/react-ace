import { connect } from 'react-redux';

import ShoppingCart from '../components/ShoppingCart';
import { showOrder } from '../actions/';

export const mapStateToProps = (state) => ({
  count: state.order.items.length,
  iconName: 'shopping_cart'
});

export const mapDispatchToProps = (dispatch) => ({
  onClick: () => dispatch(showOrder())
});

const ShoppingCartContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(ShoppingCart);

export default ShoppingCartContainer;
