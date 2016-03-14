import {EventEmitter} from 'events'
import assign from 'object-assign'
import AppDispatcher from '../dispatcher/AppDispatcher'
import {CHANGE_EVENT, ADD_TO_ORDER, REMOVE_FROM_ORDER, CHANGED_ISSUE} from '../consts'

const orders = {}

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
})

OrderStore.dispatchToken = AppDispatcher.register(payload => {
  let action = payload.action
  switch (action.type) {
    case CHANGED_ISSUE:
      if (!Object.keys(orders).indexOf(action.issue) > -1)
        orders[action.issue] = []
      break
    case ADD_TO_ORDER:
      orders[action.issueNumber].push(action.previewsCode)
      OrderStore.emitChange()
      break
    case REMOVE_FROM_ORDER:
      console.log("Removing " + action.previewsCode + " from order")
      OrderStore.emitChange()
      break
  }

  return true
})

export default OrderStore
