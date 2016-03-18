import {ADD_TO_ORDER, REMOVE_FROM_ORDER, CHANGED_ISSUE} from '../consts';
import AppDispatcher from '../dispatcher/AppDispatcher';

export function addToOrder(issueNumber, previewsCode) {
  AppDispatcher.handleAction({
    type: ADD_TO_ORDER, issueNumber: issueNumber, previewsCode: previewsCode,
  });
}

export function removeFromOrder(issueNumber, previewsCode) {
  AppDispatcher.handleAction({
    type: REMOVE_FROM_ORDER, issueNumber: issueNumber, previewsCode: previewsCode,
  });
}
