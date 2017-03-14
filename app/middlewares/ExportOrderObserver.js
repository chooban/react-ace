import fileDownload from '../utils/FileDownload';
import orderToCsv from '../utils/OrderToCsv';

export default (store) => (next) => (action) => {
  if (action.type === 'EXPORT_ORDER') {
    const state = store.getState();
    fileDownload(orderToCsv(state.order.items), `order${state.order.issue}.csv`);
  }
  next(action);
};
