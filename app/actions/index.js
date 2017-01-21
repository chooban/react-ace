import {
  createAction
} from 'redux-actions';

import {
    getLatestIssue
} from '../api/PreviewsWebApi';

const receivedIssue = createAction('RECEIVED_ISSUE_DATA');
const requestedIssue = createAction('REQUESTED_ISSUE_DATA');
const removeFromOrder = createAction('REMOVE_FROM_ORDER');
const nextPage = createAction('NEXT_PAGE');
const previousPage = createAction('PREVIOUS_PAGE');
const updateSearch = createAction('UPDATE_SEARCH');
const addToOrderCreator = createAction('ADD_TO_ORDER');
const showOrder = createAction('SHOW_ORDER');
const closeOrder = createAction('CLOSE_ORDER');
const showPreview = createAction('SHOW_PREVIEW');
const closePreview = createAction('CLOSE_PREVIEW');
const showHelp = createAction('SHOW_HELP');
const closeHelp = createAction('CLOSE_HELP');

const requestLatestIssue = () => (dispatch) => {
  dispatch(requestedIssue());

  return getLatestIssue()
    .then(receivedIssue)
    .then(dispatch);
};

const addToOrder = (orderItem) => (
  (dispatch, getStore) => {
    const catalogue = getStore().issues.data;
    const item = catalogue.find((d) => d.previewsCode === orderItem);

    dispatch(addToOrderCreator({
      previews: item.previewsCode,
      quantity: 1,
      title: item.title,
      price: item.price,
      publisher: item.publisher,
      comment: ''
    }));
  }
);

export {
    addToOrder,
    removeFromOrder,
    requestLatestIssue,
    nextPage,
    previousPage,
    updateSearch,
    requestedIssue,
    receivedIssue,
    showOrder,
    closeOrder,
    showPreview,
    closePreview,
    showHelp,
    closeHelp
};
