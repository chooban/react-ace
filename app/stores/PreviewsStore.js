import {EventEmitter} from 'events'
import assign from 'object-assign'
import AppDispatcher from '../dispatcher/AppDispatcher'
import {CHANGE_EVENT, GOT_ISSUES, GOT_ISSUE} from '../consts'

let issuesList = null
  , issuesStore = {}

let PreviewsStore = assign({}, EventEmitter.prototype, {
    emitChange() {
      this.emit(CHANGE_EVENT)
    }
  , addChangeListener(done) {
      this.on(CHANGE_EVENT, done)
  }
  , removeChangeListener(done) {
      this.removeListener(CHANGE_EVENT, done)
  }
  , getIssues() {
      return issuesList
  }
  , getIssue(issueNumber) {
      return issuesStore[issueNumber] || null
  }
})

PreviewsStore.dispatchToken = AppDispatcher.register(payload => {
  let action = payload.action
  switch (action.type) {
    case GOT_ISSUES:
      issuesList = action.all
      PreviewsStore.emitChange()
      break;
    case GOT_ISSUE:
      issuesStore[action.issue] = action.issueData
      PreviewsStore.emitChange()
      break
  }

  return true
})

export default PreviewsStore
