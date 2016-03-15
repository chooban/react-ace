import {EventEmitter} from 'events'
import assign from 'object-assign'
import AppDispatcher from '../dispatcher/AppDispatcher'
import {CHANGE_EVENT, ADD_TO_ORDER, REMOVE_FROM_ORDER, CHANGED_ISSUE} from '../consts'

const orders = {}
const keyForIssue = (issue) => {
  return "previews" + issue
}

let OrderStore = assign({}, EventEmitter.prototype, {
    emitChange() {
      this.emit(CHANGE_EVENT)
    }
  , addChangeListener(done) {
      this.on(CHANGE_EVENT, done)
  }
  , removeChangeListener(done) {
      this.removeListener(CHANGE_EVENT, done)
  }
  , isOrdered(previewsCode) {
      const components = previewsCode.split('/')
          , issueNumber = components[0]

      return (orders[keyForIssue(issueNumber)] && orders[keyForIssue(issueNumber)].indexOf(previewsCode) > -1)
    }
})

OrderStore.dispatchToken = AppDispatcher.register(payload => {
  let action = payload.action
  switch (action.type) {
    case CHANGED_ISSUE:
      if (Object.keys(orders).indexOf(keyForIssue(action.issue)) < 0)
        orders[keyForIssue(action.issue)] = []

      break
    case ADD_TO_ORDER:
      orders[keyForIssue(action.issueNumber)].push(action.previewsCode)
      OrderStore.emitChange()
      break
    case REMOVE_FROM_ORDER:
      OrderStore.emitChange()
      break
  }

  return true
})

export default OrderStore
