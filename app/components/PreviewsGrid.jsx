import React from 'react';
import PropTypes from 'prop-types';

import PreviewsLink from './PreviewsLink';
import ToggleOrder from '../containers/ToggleOrderContainer';
import {
  matchesSavedSearches
} from '../utils/CatalogueSearch';

const firstLowerCaseLetter = /(^|[^a-zA-Z\u00C0-\u017F'])([a-zA-Z\u00C0-\u017F])/g;
const capitalize = (s) => s.toLowerCase().replace(firstLowerCaseLetter, (m) => m.toUpperCase());

// Rather than being fancy about it, I'll just handle the small number of edge cases
// for acronyms in this context.
const titleFormat = (title) => (
  capitalize(title)
    .replace(/Dc /, 'DC ')
    .replace(/Idw /, 'IDW ')
    .replace(/ Tp ?/, ' TP ')
    .replace(/ Hc ?/, ' HC ')
    .replace(/Fcbd /, 'FCBD ')
);

const formatAsGBP = (v) => ({
  value: (v) ? `£${parseFloat(v).toFixed(2)}` : ''
});

const columns = [
  {
    property: 'previewsCode',
    header: 'Previews',
    cell: (v, onClick) => ({ value: <PreviewsLink previewsCode={v} showPreview={onClick} /> })
  },
  {
    property: 'title',
    header: 'Description',
    cell: (v) => ({ value: v ? titleFormat(v) : '' })
  },
  {
    property: 'price',
    header: 'Price',
    cell: formatAsGBP
  },
  {
    property: 'publisher',
    header: 'Publisher',
    cell: (v) => ({ value: v ? titleFormat(v) : '' })
  }
];

const gridDataToRows = (gridData, savedSearches, showPreview) => (
  gridData.map((row) => {
    const cells = [];
    columns.forEach((col, i) => {
      const cellContent = col.cell(row[col.property], i === 0 ? showPreview : null);
      cells.push(<td key={col.property}>{cellContent.value}</td>);
    });

    cells.push(
      <td key="ordertoggle" >
        <ToggleOrder previewsCode={row.previewsCode} ordered={row.ordered} />
      </td>
      );

    const className = matchesSavedSearches(savedSearches, row) ? 'saved' : '';

    return <tr className={className} key={row.previewsCode}>{cells}</tr>;
  })
);

const emptyRow = () => (
  <tr>
    <td
      colSpan="5"
      style={{
        textAlign: 'center'
      }}
    >
      No results found
    </td>
  </tr>
);

const PreviewsGrid = ({
    gridData,
    hasPrevious,
    hasNext,
    previousPage,
    nextPage,
    showPreview,
    savedSearches
}) => {
  const cols = columns.map((c) => <th key={c.property}>{c.header}</th>);
  cols.push(<th key="cart">&nbsp;</th>);
  const rows = (gridData.length)
      ? gridDataToRows(gridData, savedSearches, showPreview)
      : emptyRow();

  return (
    <div>
      <table className="previewsgrid">
        <thead>
          <tr>
            {cols}
          </tr>
        </thead>
        <tbody>
          {rows}
        </tbody>
      </table>
      <div className="tablecontrols">
        <a
          className="btn"
          disabled={!hasPrevious}
          onClick={previousPage}
        >
          Previous
        </a>
        <a
          className="btn"
          disabled={!hasNext}
          onClick={nextPage}
        >
          Next
        </a>
      </div>
    </div>
  );
};

PreviewsGrid.propTypes = {
  gridData: PropTypes.array,
  hasPrevious: PropTypes.bool,
  hasNext: PropTypes.bool,
  previousPage: PropTypes.func.isRequired,
  nextPage: PropTypes.func.isRequired,
  showPreview: PropTypes.func.isRequired,
  savedSearches: PropTypes.array
};

PreviewsGrid.defaultProps = {
  gridData: [],
  hasPrevious: false,
  hasNext: false,
  savedSearches: []
};

export default PreviewsGrid;
