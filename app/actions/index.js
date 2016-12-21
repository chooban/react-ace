import {
    getIssueList,
    getIssue,
    getLatestIssue
} from '../api/PreviewsWebApi';

import {
    exportOrder as exportOrderApi
} from '../api/OrdersWebApi';

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

const removeFromOrder = (orderItem) => (
    Actions.removeFromOrder(orderItem)
);

const exportOrder = (order) => (dispatch) => {
  dispatch(Actions.requestedExport());

  return exportOrderApi(order)
    .then(Actions.receivedExportedOrder())
    .then(dispatch);
};

const nextPage = () => Actions.nextPage();

const previousPage = () => Actions.previousPage();

export {
    requestIssues,
    requestIssue,
    addToOrder,
    removeFromOrder,
    exportOrder,
    requestLatestIssue,
    nextPage,
    previousPage
};
