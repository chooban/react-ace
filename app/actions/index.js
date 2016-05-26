import { getIssueList, getIssue } from '../api/PreviewsWebApi';

export const REQUESTED_ISSUES = 'REQUESTED_ISSUES';
export const RECEIVED_ISSUES = 'RECEIVED_ISSUES';

function receiveIssuesAction(issuesList) {
  return {
    type: RECEIVED_ISSUES,
    issues: issuesList
  }
}

export function requestIssues() {
  return function(dispatch) {
    dispatch({
      type: REQUESTED_ISSUES
    });

    return getIssueList()
            .then(receiveIssuesAction)
            .then(dispatch);
  }
}

export function requestIssue(issueNumber) {
  return function(dispatch) {
    dispatch({
      type: 'REQUESTED_ISSUE_DATA',
      issueNumber: issueNumber
    });

    return getIssue(issueNumber)
            .then((issueData) => {
              return {
                type: 'RECEIVED_ISSUE_DATA',
                issueNumber: issueNumber,
                issueData: issueData
              }
            })
            .then(dispatch);
  }
}
