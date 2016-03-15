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
          , key = keyForIssue(issueNumber)

      console.log(JSON.stringify(orders))
      return (orders[key] && orders[key].indexOf(previewsCode) > -1)
    }
})

OrderStore.dispatchToken = AppDispatcher.register(payload => {
  const action = payload.action
  const key = keyForIssue(action.issueNumber)

  switch (action.type) {
    case ADD_TO_ORDER:
      if (Object.keys(orders).indexOf(key) < 0) orders[key] = []

      orders[key].push(action.previewsCode)
      OrderStore.emitChange()
      break
    case REMOVE_FROM_ORDER:
      const a = orders[key]
      a.splice(a.indexOf(action.previewsCode), 1)
      OrderStore.emitChange()
      break
  }

  return true
})

export default OrderStore
