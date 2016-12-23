import { connect } from 'react-redux';
import {
  addToOrder,
  removeFromOrder,
  nextPage,
  previousPage,
  updateSearch
} from '../actions';
import PreviewsGrid from '../components/PreviewsGrid';

const props = {
  gridData: []
};

const getRecords = (gridConfig, catalogue) => {
  let records = catalogue;

  const publisherOrTitleMatches = (regex) =>
    (d) => regex.test(d.publisher) || regex.test(d.title);

  if (gridConfig.searchTerm) {
    const regex = new RegExp(`.*${gridConfig.searchTerm}.*`, 'ig');
    records = catalogue.filter(publisherOrTitleMatches(regex));
  }

  return records;
};

const mapStateToProps = (state) => {
  const gridConfig = state.gridConfig;
  const records = getRecords(gridConfig, state.issues.data);
  const recordsStart = (gridConfig.page - 1) * gridConfig.pageSize;
  const recordsEnd = recordsStart + gridConfig.pageSize;
  const recordsToDisplay = records.slice(recordsStart, recordsEnd);

  const gridData = recordsToDisplay.map((lineItem) => {
    const orderIndex = state.order.items.findIndex((d) => d.previews === lineItem.previewsCode);

    return Object.assign(
        {},
        lineItem,
        { onorder: orderIndex > -1 }
        );
  });

  return Object.assign({}, props, {
    gridData,
    hasPrevious: gridConfig.page > 1,
    hasNext: recordsStart + gridConfig.pageSize <= records.length
  });
};

export const mapDispatchToProps = (dispatch) => ({
  nextPage: () => dispatch(nextPage()),
  previousPage: () => dispatch(previousPage()),
  onItemSelected: (previewsCode, onOrder) => {
    if (!onOrder) dispatch(addToOrder(previewsCode));
    else dispatch(removeFromOrder(previewsCode));
  },
  onSearchUpdate: (d) => dispatch(updateSearch(d))
});

const PreviewsGridContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(PreviewsGrid);

export default PreviewsGridContainer;
