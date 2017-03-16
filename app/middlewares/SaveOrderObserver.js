const triggers = [
  'ADD_TO_ORDER',
  'REMOVE_FROM_ORDER'
];

export default (store) => (next) => (action) => {
  const result = next(action);

  if (triggers.includes(action.type)) {
    const state = store.getState();
    localStorage.setItem('saved_order', JSON.stringify(state.order));
  }

  return result;
};
