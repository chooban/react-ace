import { EventEmitter } from 'events';
import assign from 'object-assign';
import Ramda from 'ramda';
import AppDispatcher from '../dispatcher/AppDispatcher';
import { CHANGE_EVENT, GOT_ISSUES, GOT_ISSUE, CHANGED_ISSUE } from '../consts';

let issuesList = null;
let currentIssue = null;

let PreviewsStore = assign({}, EventEmitter.prototype, {
  emitChange() {
    this.emit(CHANGE_EVENT);
  },

  addChangeListener(done) {
    this.on(CHANGE_EVENT, done);
  },

  removeChangeListener(done) {
    this.removeListener(CHANGE_EVENT, done);
  },

  getIssues() {
    return issuesList;
  },

  getCurrentIssue() {
    return currentIssue;
  },
});

PreviewsStore.dispatchToken = AppDispatcher.register(payload => {
  let action = payload.action;
  switch (action.type) {
    case GOT_ISSUES:
      issuesList = action.all.sort((a, b) => b.issue - a.issue);
      PreviewsStore.emitChange();
      break;
    case GOT_ISSUE:
      currentIssue = action.issueData;
      PreviewsStore.emitChange();
      break;
  }

  return true;
});

export default PreviewsStore;
