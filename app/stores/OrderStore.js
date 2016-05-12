import { EventEmitter } from 'events';
import assign from 'object-assign';
import AppDispatcher from '../dispatcher/AppDispatcher';
import { CHANGE_EVENT, ADD_TO_ORDER, REMOVE_FROM_ORDER, CHANGED_ISSUE } from '../consts';

const orders = {};
const keyForIssue = issue => 'previews' + issue;

let currentIssue = null;

let OrderStore = assign({}, EventEmitter.prototype, {
  emitChange() {
    this.emit(CHANGE_EVENT);
  },

  addChangeListener(done) {
    this.on(CHANGE_EVENT, done);
  },

  removeChangeListener(done) {
    this.removeListener(CHANGE_EVENT, done);
  },

  getCurrentIssue() {
    return currentIssue;
  },

  isOrdered(previewsCode) {
    const components = previewsCode.split('/');
    const issueNumber = components[0];
    const key = keyForIssue(issueNumber);

    return (orders[key] && orders[key].indexOf(previewsCode) > -1);
  },

  getCurrentOrderMetadata() {
    var currentOrder = orders[keyForIssue(currentIssue)];

    return currentOrder.length;
  },
});

const registeredCallback = (payload) => {
  const action = payload.action;
  const key = keyForIssue(action.issueNumber);

  switch (action.type) {
    case CHANGED_ISSUE:
      currentIssue = action.issueNumber;
      break;
    case ADD_TO_ORDER:
      if (Object.keys(orders).indexOf(key) < 0) orders[key] = [];

      orders[key].push(action.previewsCode);
      OrderStore.emitChange();
      break;
    case REMOVE_FROM_ORDER:
      const a = orders[key];
      a.splice(a.indexOf(action.previewsCode), 1);
      OrderStore.emitChange();
      break;
  }

  return true;
};

OrderStore.dispatchToken = AppDispatcher.register(registeredCallback);

export default OrderStore;
