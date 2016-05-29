import { requestIssue } from '../actions';

let actors = [
  fetchInitialGridData
];
let acting = false;

function fetchInitialGridData(state, dispatch) {
  if (state.issues.issuesList.length && !state.issues.data.length) {
    dispatch(requestIssue(state.issues.issuesList[0]));
  }
}

export default function(store) {
  store.subscribe(() => {
    if (!acting) {
      acting = true;
      actors.forEach((a) => a(store.getState(), store.dispatch));
      acting = false;
    }
  });
}

