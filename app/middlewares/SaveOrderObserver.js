const triggers = [
  'ADD_TO_ORDER',
  'REMOVE_FROM_ORDER',
  'CLEAR_ORDER'
];

export default (storage = localStorage) => (store) => (next) => (action) => {
  const result = next(action);

  if (triggers.includes(action.type)) {
    const state = store.getState();
    storage.setItem('saved_order', JSON.stringify(state.order));
  }

  return result;
};
