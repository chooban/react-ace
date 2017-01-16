import { connect } from 'react-redux';
import {
  nextPage,
  previousPage,
  showPreview
} from '../actions';

import {
  searchCatalogue
} from './CatalogueSearch';

import PreviewsGrid from '../components/PreviewsGrid';

const props = {
  gridData: []
};

const getRecords = (gridConfig, catalogue) => (
  (gridConfig.searchTerm)
    ? searchCatalogue(gridConfig.searchTerm, catalogue)
    : catalogue
);

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
  showPreview: (p) => dispatch(showPreview(p))
});

const PreviewsGridContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(PreviewsGrid);

export default PreviewsGridContainer;
