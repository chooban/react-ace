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

const formatAsGBP = (v) => {
  const currency = (c) => c.toLocaleString(null, { style: 'currency', currency: 'GBP' });
  return {
    value: (v) ? `£${currency(v)}` : ''
  };
};

const columns = [
  {
    property: 'previewsCode',
    header: 'Previews Code',
    cell: (v) => ({ value: <PreviewsLink previewsCode={v} /> })
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
    property: 'reducedFrom',
    header: 'Was',
    cell: formatAsGBP
  },
  {
    property: 'publisher',
    header: 'Publisher',
    cell: (v) => ({ value: v ? titleFormat(v) : '' })
  }
];

export default class PreviewsGrid extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    const cols = columns.map((c) => <th key={c.property}>{c.header}</th>);
    const rows = this.props.gridData.map((row) => {
      const cells = [];
      columns.forEach((col, i) => {
        const cellContent = col.cell(row[col.property]);
        cells.push(<td key={i}>{cellContent.value}</td>);
      });

      cells.push(
        <td
          key="ordertoggle"
        >
          <ToggleOrder
            ordered={row.onorder}
            previewsCode={row.previewsCode}
            onItemSelected={this.props.onItemSelected}
          />
        </td>
      );
      return <tr key={row.previewsCode}>{cells}</tr>;
    });

    return (
      <div>
        <div className="gridsearch">
          <label
            htmlFor="search"
          >
            Search:
            <input
              type="text"
              name="search"
              placeholder="Search"
              size="25"
              onInput={(e) => this.props.onSearchUpdate(e.target.value)}
            />
          </label>
        </div>
        <table>
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
          disabled={!this.props.hasPrevious}
          onClick={this.props.previousPage}
        />
        <input
          type="button"
          value="Next"
          disabled={!this.props.hasNext}
          onClick={this.props.nextPage}
        />
      </div>
    );
  }
}

PreviewsGrid.propTypes = {
  gridData: React.PropTypes.array,
  onItemSelected: React.PropTypes.func,
  hasPrevious: React.PropTypes.bool,
  hasNext: React.PropTypes.bool,
  previousPage: React.PropTypes.func,
  nextPage: React.PropTypes.func,
  onSearchUpdate: React.PropTypes.func
};
