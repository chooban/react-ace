import React from 'react';
import PropTypes from 'prop-types';

import PreviewsLink from './PreviewsLink';
import ClickableIcon from './ClickableIcon';

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
    property: 'previews',
    header: 'Previews',
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

const OrderEditor = ({ items, onRemoveItem }) => {
  const rows = [];
  let total = 0;
  items.forEach((item) => {
    const cells = [];
    columns.forEach((c) => {
      const content = c.cell(item[c.property]);
      cells.push(<td key={c.property}>{content.value}</td>);
    });

    const removeItem = () => onRemoveItem(item.previews);

    cells.push(<td key="remove" className="remove">
      <ClickableIcon
        className="remove"
        iconName="remove_shopping_cart"
        onClick={removeItem}
      />
    </td>
    );

    rows.push(<tr key={item.previews}>{ cells }</tr>);

    total += parseFloat(item.price);
  });

  const orderTotal = formatAsGBP(total).value;

  rows.push(<tr className="totals" key={'total'}>
    <td colSpan="2">Total</td>
    <td colSpan="2">{orderTotal}</td>
  </tr>);

  const headers = columns.map((c) => <th key={c.property}>{c.header}</th>);

  return (<table className="ordereditor">
    <thead>
      <tr>{ headers }</tr>
    </thead>
    <tbody>
      { rows }
    </tbody>
  </table>);
};

OrderEditor.propTypes = {
  items: PropTypes.instanceOf(Array),
  onRemoveItem: PropTypes.func.isRequired
};

OrderEditor.defaultProps = {
  items: []
};

export default OrderEditor;
