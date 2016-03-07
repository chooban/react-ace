import {EventEmitter} from 'events'
import assign from 'object-assign'
import AppDispatcher from '../dispatcher/AppDispatcher'
import {CHANGE_EVENT, CHOSE_ISSUE} from '../consts'

let data = null

let ChosenIssueStore = assign({}, EventEmitter.prototype, {
    emitChange() {
      console.log("Emitting a change")
      this.emit(CHANGE_EVENT)
    }
  , addChangeListener(done) {
      this.on(CHANGE_EVENT, done)
  }
  , removeChangeListener(done) {
      this.removeListener(CHANGE_EVENT, done)
  }
  , getChosenIssue() {
      return data
  }
})

ChosenIssueStore.dispatchToken = AppDispatcher.register(payload => {
  console.log("Dispatching token :", JSON.stringify(payload))
  let action = payload.action
  switch (action.type) {
    case CHOSE_ISSUE:
      data = action.issue
      console.log("Emitting a change from the chosen issue store")
      ChosenIssueStore.emitChange()
      break;
  }

  return true
})

export default ChosenIssueStore
