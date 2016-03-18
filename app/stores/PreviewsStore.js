import {EventEmitter} from 'events';
import assign from 'object-assign';
import Ramda from 'ramda';
import AppDispatcher from '../dispatcher/AppDispatcher';
import {CHANGE_EVENT, GOT_ISSUES, GOT_ISSUE, CHANGED_ISSUE} from '../consts';

const issuesStore = {};

let issuesList = null;
let currentIssue;

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
      issuesList = action.all.sort(function (a, b) {
        return b.issue - a.issue;
      });

      PreviewsStore.emitChange();
      break;
    case GOT_ISSUE:
      currentIssue = csvToModel(action.issueData);
      PreviewsStore.emitChange();
      break;
  }

  return true;
});

function csvToModel(csvData) {
  return Ramda.map(rowToItemModel, csvData);

  function rowToItemModel(row) {
    const columnNames = [
      'id', 'title', 'price', 'listPrice', 'publisher',
    ];
    return Ramda.zipObj(columnNames, Ramda.map(Ramda.nth(Ramda.__, row), [0, 1, 3, 5, 6]));
  }
}

export default PreviewsStore;
