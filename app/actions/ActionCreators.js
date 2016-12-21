const RECEIVED_ISSUES = 'RECEIVED_ISSUES';
const REQUESTED_ISSUES = 'REQUESTED_ISSUES';

const receivedIssues = (issues) => ({
  type: RECEIVED_ISSUES,
  issues
});

const requestedIssues = () => ({
  type: REQUESTED_ISSUES
});

const receivedIssue = (issueData) => ({
  type: 'RECEIVED_ISSUE_DATA',
  issueData
});

const requestedIssue = (issueNumber) => ({
  type: 'REQUESTED_ISSUE_DATA',
  issueNumber
});

const addToOrder = (orderItem) => ({
  type: 'ADD_TO_ORDER',
  orderItem
});

const removeFromOrder = (orderItem) => ({
  type: 'REMOVE_FROM_ORDER',
  orderItem
});

const requestedExport = () => ({
  type: 'EXPORTING_ORDER'
});

const receivedExportedOrder = (order) => ({
  type: 'RECEIVED_EXPORT',
  order
});

const nextPage = () => ({
  type: 'NEXT_PAGE'
});

const previousPage = () => ({
  type: 'PREVIOUS_PAGE'
});

export {
  receivedIssues,
  receivedIssue,
  requestedIssues,
  requestedIssue,
  addToOrder,
  removeFromOrder,
  requestedExport,
  receivedExportedOrder,
  nextPage,
  previousPage
};

export {
  RECEIVED_ISSUES,
  REQUESTED_ISSUES
};
