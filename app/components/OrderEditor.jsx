import React from 'react';
import PreviewsLink from './PreviewsLink';

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
    property: 'previews',
    header: 'Previews Code',
    cell: (v) => ({ value: <PreviewsLink previewsCode={v} /> })
  },
  {
    property: 'title',
    header: 'Title',
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

const OrderEditor = ({ items }) => {
  const rows = [];
  items.forEach((item) => {
    const cells = [];
    columns.forEach((c, i) => {
      const content = c.cell(item[c.property]);
      cells.push(<td key={i}>{content.value}</td>);
    });

    rows.push(<tr key={item.previews}>{ cells }</tr>);
  });

  const headers = columns.map((c) => <th key={c.property}>{c.header}</th>);

  return (<table>
    <thead>
      <tr>{ headers }</tr>
    </thead>
    <tbody>
      { rows }
    </tbody>
  </table>);
};

OrderEditor.propTypes = {
  items: React.PropTypes.instanceOf(Array)
};

export default OrderEditor;
