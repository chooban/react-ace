import { connect } from 'react-redux';
import { addToOrder, removeFromOrder, nextPage, previousPage } from '../actions';
import PreviewsGrid from '../components/PreviewsGrid';

const props = {
  gridData: []
};

const mapStateToProps = (state) => {
  const gridConfig = state.gridConfig;
  const recordsStart = (gridConfig.page - 1) * gridConfig.pageSize;
  const records = state.issues.data.slice(recordsStart, recordsStart + gridConfig.pageSize);
  const gridData = records.map((lineItem) => (
    Object.assign({}, lineItem, { onorder: state.order.items.has(lineItem.previewsCode) })
  ));

  return Object.assign({}, props, {
    gridData,
    hasPrevious: gridConfig.page > 1,
    hasNext: recordsStart + gridConfig.pageSize < state.issues.data.length
  });
};

export const mapDispatchToProps = (dispatch) => ({
  nextPage: () => dispatch(nextPage()),
  previousPage: () => dispatch(previousPage()),
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
