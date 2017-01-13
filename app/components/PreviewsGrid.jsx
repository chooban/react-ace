import React from 'react';

import PreviewsLink from './PreviewsLink';
import ToggleOrder from '../containers/ToggleOrderContainer';

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

const PreviewsGrid = ({
    gridData,
    onItemSelected,
    hasPrevious,
    hasNext,
    previousPage,
    nextPage,
    showPreview
}) => {
  const cols = columns.map((c) => <th key={c.property}>{c.header}</th>);
  const rows = gridData.map((row) => {
    const cells = [];
    columns.forEach((col, i) => {
      const cellContent = col.cell(row[col.property], i === 0 ? showPreview : null);
      cells.push(<td key={i}>{cellContent.value}</td>);
    });

    cells.push(
      <td
        key="ordertoggle"
      >
        <ToggleOrder
          ordered={row.onorder}
          previewsCode={row.previewsCode}
          onItemSelected={onItemSelected}
        />
      </td>
      );
    return <tr key={row.previewsCode}>{cells}</tr>;
  });

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
      <input
        type="button"
        value="Previous"
        disabled={!hasPrevious}
        onClick={previousPage}
      />
      <input
        type="button"
        value="Next"
        disabled={!hasNext}
        onClick={nextPage}
      />
    </div>
  );
};

PreviewsGrid.propTypes = {
  gridData: React.PropTypes.array,
  onItemSelected: React.PropTypes.func,
  hasPrevious: React.PropTypes.bool,
  hasNext: React.PropTypes.bool,
  previousPage: React.PropTypes.func,
  nextPage: React.PropTypes.func,
  showPreview: React.PropTypes.func
};

export default PreviewsGrid;
