import {
    getIssueList,
    getIssue,
    getLatestIssue
} from '../api/PreviewsWebApi';

import * as Actions from './ActionCreators';

const requestIssues = () => (
    (dispatch) => {
      dispatch(Actions.requestedIssues());

      return getIssueList()
          .then(Actions.receivedIssues)
          .then(dispatch);
    }
);

const requestIssue = (issueNumber) => (dispatch) => {
  dispatch(Actions.requestedIssue(issueNumber));

  return getIssue(issueNumber)
      .then(Actions.receivedIssue)
      .then(dispatch);
};

const requestLatestIssue = () => (dispatch) => (
    getLatestIssue()
      .then(Actions.receivedIssue)
      .then(dispatch)
);

const addToOrder = (orderItem) => (
    Actions.addToOrder(orderItem)
);

export {
    requestIssues,
    requestIssue,
    addToOrder,
    requestLatestIssue
};
