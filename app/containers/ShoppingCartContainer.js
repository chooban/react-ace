import { connect } from 'react-redux';

import ClickableIcon from '../components/ClickableIcon';
import { showOrder } from '../actions/';

const determineClassName = (items) => (
  `ordersummary${items.length > 0 ? ' hasitems' : ''}`
);

export const mapStateToProps = (state) => ({
  className: determineClassName(state.order.items),
  iconName: 'shopping_cart'
});

export const mapDispatchToProps = (dispatch) => ({
  onClick: () => dispatch(showOrder())
});

const ShoppingCartContainer = connect(
    mapStateToProps,
    mapDispatchToProps
)(ClickableIcon);

export default ShoppingCartContainer;
