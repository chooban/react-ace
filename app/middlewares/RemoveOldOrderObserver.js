import { clearOrder } from '../actions/';

const triggers = [
  'RECEIVED_ISSUE_DATA'
];

export default (store) => (next) => (action) => {
  if (triggers.includes(action.type)) {
    const { file } = action.payload;
    const state = store.getState();

    if (file !== state.order.issue) {
      store.dispatch(clearOrder());
    }
  }

  return next(action);
};
