import initialState from './InitialState';

export default function gridConfig(state = initialState.gridConfig, action) {
  switch (action.type) {
    case 'NEXT_PAGE':
      return Object.assign({}, state, {
        page: state.page + 1,
        pageSize: state.pageSize
      });
    case 'PREVIOUS_PAGE':
      return Object.assign({}, state, {
        page: Math.max(1, state.page - 1),
        pageSize: state.pageSize
      });
    case 'PERFORM_SAVED_SEARCH':
    case 'UPDATE_SEARCH': {
      let { page } = state;
      let searchTerm = action.payload || '';

      if (searchTerm.length === 0) {
        searchTerm = undefined;
        page = 1;
      }

      if (searchTerm && !state.searchTerm) {
        page = 1;
      }
      return Object.assign({}, state, {
        searchTerm,
        page
      });
    }
    default:
      return state;
  }
}
