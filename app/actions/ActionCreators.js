export const RECEIVED_ISSUES = 'RECEIVED_ISSUES';
export const REQUESTED_ISSUES = 'REQUESTED_ISSUES';

export const receivedIssues = (issues) => (
  {
    type: RECEIVED_ISSUES,
    issues
  }
);

export const requestedIssues = () => ({
  type: REQUESTED_ISSUES
});

export const receivedIssue = (issueData) => (
  {
    type: 'RECEIVED_ISSUE_DATA',
    issueData
  }
);

export const requestedIssue = (issueNumber) => (
  {
    type: 'REQUESTED_ISSUE_DATA',
    issueNumber
  }
);
