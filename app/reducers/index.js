import { RECEIVED_ISSUES, REQUESTED_ISSUES } from '../actions';

const initialState = {
  issues: {
    isFetching: false,
    issuesList: [],
    data: []
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

export default function app(state = initialState, action) {
  return {
    issues: issues(state.issues, action)
  };
}
