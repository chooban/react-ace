import { getIssueList, getIssue } from '../api/PreviewsWebApi';
import * as Actions from './ActionCreators';

export function requestIssues() {
  return (dispatch) => {
    dispatch(Actions.requestedIssues());

    return getIssueList()
            .then(Actions.receivedIssues)
            .then(dispatch);
  };
}

export function requestIssue(issueNumber) {
  return (dispatch) => {
    dispatch(Actions.requestedIssue(issueNumber));

    return getIssue(issueNumber)
            .then(Actions.receivedIssue)
            .then(dispatch);
  };
}
