import { connect } from 'react-redux';
import { addToOrder, removeFromOrder } from '../actions';
import PreviewsGrid from '../components/PreviewsGrid';

const props = {
  gridData: []
};

const mapStateToProps = (state) => {
  const gridData = state.issues.data.map((lineItem) => (
    Object.assign({}, lineItem, { onorder: state.order.items.has(lineItem.previewsCode) })
  ));

  return Object.assign({}, props, {
    gridData
  });
};

export const mapDispatchToProps = (dispatch) => ({
  onItemSelected: (previewsCode, onOrder) => {
    if (!onOrder) dispatch(addToOrder(previewsCode));
    else dispatch(removeFromOrder(previewsCode));
  }
});

const PreviewsGridContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(PreviewsGrid);

export default PreviewsGridContainer;
