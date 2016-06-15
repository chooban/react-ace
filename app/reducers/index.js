import { REQUESTED_ISSUES } from '../actions';
import { RECEIVED_ISSUES } from '../actions/ActionCreators';

const initialState = {
  issues: {
    isFetching: false,
    issuesList: [],
    data: []
  },
  order: {
    items: []
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
    case 'ADD_TO_ORDER':
      return Object.assign({}, state, {
        items: [...state.items, action.orderItem]
      });
    default:
      return state;
  }
}

export default function app(state = initialState, action) {
  return {
    issues: issues(state.issues, action),
    order: order(state.order, action)
  };
}
