import initialState from './InitialState';

export default function issues(state = initialState.issues, action) {
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

