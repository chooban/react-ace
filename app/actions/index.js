import { getIssueList, getIssue } from '../api/PreviewsWebApi';

export const REQUESTED_ISSUES = 'REQUESTED_ISSUES';
export const RECEIVED_ISSUES = 'RECEIVED_ISSUES';

const receiveIssuesAction = (issuesList) => (
  {
    type: RECEIVED_ISSUES,
    issues: issuesList
  }
);

export function requestIssues() {
  return (dispatch) => {
    dispatch({
      type: REQUESTED_ISSUES
    });

    return getIssueList()
            .then(receiveIssuesAction)
            .then(dispatch);
  };
}

export function requestIssue(issueNumber) {
  const receivedIssueAction = (issueData) => (
    {
      type: 'RECEIVED_ISSUE_DATA',
      issueNumber,
      issueData
    }
  );

  return (dispatch) => {
    dispatch({
      type: 'REQUESTED_ISSUE_DATA',
      issueNumber
    });

    return getIssue(issueNumber)
            .then(receivedIssueAction)
            .then(dispatch);
  };
}
