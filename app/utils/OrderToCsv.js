const sprintf = require('sprintf');

const headers = 'Previews Code,Quantity,Title,Price,Publisher,Comment\n';
const row = '%s,%d,%s,%s,%s,%s\n';

export default function (order) {
  let csv = headers;
  csv += order.reduce((acc, lineItem) => acc + sprintf(row, lineItem.previews,
        lineItem.quantity,
        lineItem.title,
        lineItem.price,
        lineItem.publisher,
        lineItem.comment), '');

  const orderTotal = order.reduce((acc, lineItem) => (
        acc + (lineItem.quantity * +lineItem.price)
    ), 0);

  csv += `,,Total,${orderTotal.toFixed(2)},\n`;
  csv += '\nGenerated by Ace My Order';

  return csv;
}
