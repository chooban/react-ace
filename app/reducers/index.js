const initialState = {
  issues: {
    isFetching: false,
    issuesList: [],
    data: []
  },
  order: {
    issue: undefined,
    items: []
  },
  gridConfig: {
    pageSize: 25,
    page: 1,
    searchTerm: undefined
  },
  ui: {
    showOrder: false,
    showItemPreview: false,
    showHelp: false,
    itemPreview: undefined,
    showSavedSearches: false
  },
  user: {
    profile: null
  }
};

function issues(state = initialState.issues, action) {
  switch (action.type) {
    case 'REQUESTED_ISSUE_DATA':
      return Object.assign({}, state, {
        isFetching: true
      });
    case 'RECEIVED_ISSUE_DATA':
      return Object.assign({}, state, {
        isFetching: false,
        data: action.payload.contents
      });
    default:
      return state;
  }
}

function order(state = initialState.order, action) {
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
    default:
      return state;
  }
}

function gridConfig(state = initialState.gridConfig, action) {
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
    case 'UPDATE_SEARCH': {
      let page = state.page;
      let searchTerm = action.payload || '';
      searchTerm = searchTerm.trim();

      if (searchTerm.length === 0) searchTerm = undefined;

      if (searchTerm && !state.searchTerm) {
        page = 1;
      } else if (!searchTerm) {
        page = 1;
      }
      return Object.assign({}, state, {
        searchTerm,
        page
      });
    }
    default: return state;
  }
}

function ui(state = initialState.ui, action) {
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
      return Object.assign({}, state, {
        showItemPreview: false
      });
    case 'REMOVE_FROM_ORDER':
      return Object.assign({}, state, {
        showItemPreview: false
      });
    case 'SHOW_SAVED_SEARCHES':
      return Object.assign({}, state, {
        showSavedSearches: true
      });
    case 'CLOSE_SAVED_SEARCHES':
      return Object.assign({}, state, {
        showSavedSearches: false
      });
    default: return state;
  }
}

function user(state = initialState.user, action) {
  switch (action.type) {
    case 'SET_USER_PROFILE': {
      const profile = Object.assign({}, action.payload,
        {
          savedsearches: [
            'rick',
            'bad machinery'
          ]
        }
      );
      return Object.assign({}, state, {
        profile
      });
    }
    case 'LOGOUT':
      return Object.assign({}, state, {
        profile: null
      });
    case 'DELETE_SAVED_SEARCH': {
      const searches = state.profile.savedsearches.slice(0);
      const idx = searches.indexOf(action.payload);
      if (idx > -1) {
        searches.splice(idx, 1);
      }
      const profile = Object.assign({}, state.profile, {
        savedsearches: searches
      });
      return Object.assign({}, state, {
        profile
      });
    }
    default: return state;
  }
}

export default function app(state = initialState, action) {
  return {
    issues: issues(state.issues, action),
    order: order(state.order, action),
    gridConfig: gridConfig(state.gridConfig, action),
    ui: ui(state.ui, action),
    user: user(state.user, action)
  };
}
