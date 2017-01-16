import { connect } from 'react-redux';

import {
  addToOrder,
  removeFromOrder
} from '../actions/';

import ToggleOrderComponent from '../components/ToggleOrder';

const mapStateToProps = (state, props) => ({
  ordered: !!state.order.items.find((e) => e.previews === props.previewsCode)
});

export const mapDispatchToProps = (dispatch) => ({
  onItemSelected: (previewsCode, onOrder) => {
    if (!onOrder) dispatch(addToOrder(previewsCode));
    else dispatch(removeFromOrder(previewsCode));
  }
});

const ToggleOrderContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(ToggleOrderComponent);

export default ToggleOrderContainer;
