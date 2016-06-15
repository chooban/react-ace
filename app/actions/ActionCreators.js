const RECEIVED_ISSUES = 'RECEIVED_ISSUES';
const REQUESTED_ISSUES = 'REQUESTED_ISSUES';

const receivedIssues = (issues) => (
  {
    type: RECEIVED_ISSUES,
    issues
  }
);

const requestedIssues = () => ({
  type: REQUESTED_ISSUES
});

const receivedIssue = (issueData) => (
  {
    type: 'RECEIVED_ISSUE_DATA',
    issueData
  }
);

const requestedIssue = (issueNumber) => (
  {
    type: 'REQUESTED_ISSUE_DATA',
    issueNumber
  }
);

export {
  receivedIssues,
  receivedIssue,
  requestedIssues,
  requestedIssue
};

export {
  RECEIVED_ISSUES,
  REQUESTED_ISSUES
};
