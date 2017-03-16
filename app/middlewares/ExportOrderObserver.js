import fileDownload from '../utils/FileDownload';
import orderToCsv from '../utils/OrderToCsv';

const triggers = ['EXPORT_ORDER'];

export default (store) => (next) => (action) => {
  if (triggers.includes(action.type)) {
    const state = store.getState();
    fileDownload(orderToCsv(state.order.items), `order${state.order.issue}.csv`);
  }
  return next(action);
};
