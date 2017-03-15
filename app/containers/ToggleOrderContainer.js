import { connect } from 'react-redux';

import {
  addToOrder,
  removeFromOrder
} from '../actions/';

import ToggleOrderComponent from '../components/ToggleOrder';

export const mapDispatchToProps = (dispatch) => ({
  onItemSelected: (previewsCode, onOrder) => {
    if (!onOrder) dispatch(addToOrder(previewsCode));
    else dispatch(removeFromOrder(previewsCode));
  }
});

const ToggleOrderContainer = connect(
  null,
  mapDispatchToProps
)(ToggleOrderComponent);

export default ToggleOrderContainer;
