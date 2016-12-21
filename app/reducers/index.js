import { RECEIVED_ISSUES, REQUESTED_ISSUES } from '../actions/ActionCreators';

const initialState = {
  issues: {
    isFetching: false,
    issuesList: [],
    data: []
  },
  order: {
    items: new Set()
  },
  gridConfig: {
    pageSize: 25,
    page: 1
  }
};

function issues(state = initialState.issues, action) {
  switch (action.type) {
    case REQUESTED_ISSUES:
      return Object.assign({}, state, {
        isFetching: true
      });
    case RECEIVED_ISSUES:
      return Object.assign({}, state, {
        isFetching: false,
        issuesList: action.issues
      });
    case 'REQUESTED_ISSUE_DATA':
      return Object.assign({}, state, {
        isFetching: true
      });
    case 'RECEIVED_ISSUE_DATA':
      return Object.assign({}, state, {
        isFetching: false,
        data: action.issueData
      });
    default:
      return state;
  }
}

function order(state = initialState.order, action) {
  switch (action.type) {
    case 'ADD_TO_ORDER': {
      const nextItems = new Set(state.items);
      nextItems.add(action.orderItem);

      return Object.assign({}, state, {
        items: nextItems
      });
    }
    case 'REMOVE_FROM_ORDER': {
      if (state.items.has(action.orderItem)) {
        const items = new Set(state.items);
        items.delete(action.orderItem);
        return Object.assign({}, state, { items });
      }
      return state;
    }
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
    default: return state;
  }
}

export default function app(state = initialState, action) {
  return {
    issues: issues(state.issues, action),
    order: order(state.order, action),
    gridConfig: gridConfig(state.gridConfig, action)
  };
}
