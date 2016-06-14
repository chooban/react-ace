import { requestIssue } from '../actions';

function fetchInitialGridData(state, dispatch) {
  if (state.issues.issuesList.length && !state.issues.data.length) {
    dispatch(requestIssue(state.issues.issuesList[0]));
  }
}

const actors = [
  fetchInitialGridData
];
let acting = false;

export default (store) => {
  store.subscribe(() => {
    if (!acting) {
      acting = true;
      actors.forEach((a) => a(store.getState(), store.dispatch));
      acting = false;
    }
  });
};

