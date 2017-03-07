import initialState from './InitialState';

export default function ui(state = initialState.ui, action) {
  switch (action.type) {
    case 'SHOW_ORDER':
      return Object.assign({}, state, {
        showOrder: true
      });
    case 'CLOSE_ORDER':
      return Object.assign({}, state, {
        showOrder: false
      });
    case 'SHOW_PREVIEW':
      return Object.assign({}, state, {
        showItemPreview: true,
        itemPreview: action.payload
      });
    case 'CLOSE_PREVIEW':
      return Object.assign({}, state, {
        showItemPreview: false
      });
    case 'SHOW_HELP':
      return Object.assign({}, state, {
        showHelp: true
      });
    case 'CLOSE_HELP':
      return Object.assign({}, state, {
        showHelp: false
      });
    case 'ADD_TO_ORDER':
    case 'REMOVE_FROM_ORDER':
      return Object.assign({}, state, {
        showItemPreview: false
      });
    case 'SHOW_SAVED_SEARCHES':
      return Object.assign({}, state, {
        showSavedSearches: true
      });
    case 'PERFORM_SAVED_SEARCH':
    case 'CLOSE_SAVED_SEARCHES':
      return Object.assign({}, state, {
        showSavedSearches: false
      });
    default: return state;
  }
}
