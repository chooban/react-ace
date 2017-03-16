import initialState from './InitialState';

export default function orderReducer(state = initialState.order, action) {
  switch (action.type) {
    case 'ADD_TO_ORDER': {
      const idx = state.items.findIndex((d) => d.previews === action.payload.previews);
      if (idx > -1) return state;

      const nextItems = state.items.slice(0);
      nextItems.push(action.payload);

      return Object.assign({}, state, {
        items: nextItems
      });
    }
    case 'REMOVE_FROM_ORDER': {
      const idx = state.items.findIndex((d) => d.previews === action.payload);
      if (idx > -1) {
        const items = state.items.slice(0, idx).concat(state.items.slice(idx + 1));
        return Object.assign({}, state, { items });
      }
      return state;
    }
    case 'RECEIVED_ISSUE_DATA':
      return Object.assign({}, state, {
        issue: action.payload.file
      });
    case 'CLEAR_ORDER':
      return Object.assign({}, state, initialState.order);
    default:
      return state;
  }
}

