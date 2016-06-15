import { getIssueList, getIssue } from '../api/PreviewsWebApi';
import * as Actions from './ActionCreators';

export const requestIssues = () => (
  (dispatch) => {
    dispatch(Actions.requestedIssues());

    return getIssueList()
            .then(Actions.receivedIssues)
            .then(dispatch);
  }
);

export const requestIssue = (issueNumber) => (
  (dispatch) => {
    dispatch(Actions.requestedIssue(issueNumber));

    return getIssue(issueNumber)
            .then(Actions.receivedIssue)
            .then(dispatch);
  }
);
