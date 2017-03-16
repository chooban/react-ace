import initialState from './InitialState';

export default function (storage = localStorage) {
  const storedOrder = storage.getItem('saved_order');

  if (storedOrder) {
    return Object.assign({}, initialState, {
      order: JSON.parse(storedOrder)
    });
  }

  return Object.assign({}, initialState);
}
