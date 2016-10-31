import { connect } from 'react-redux';
import { addToOrder } from '../actions';
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

const mapDispatchToProps = (dispatch) => ({
  onItemSelected: (d) => dispatch(addToOrder(d))
});

const PreviewsGridContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(PreviewsGrid);

export default PreviewsGridContainer;
