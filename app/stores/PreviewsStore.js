import {EventEmitter} from 'events'
import assign from 'object-assign'
import AppDispatcher from '../dispatcher/AppDispatcher'

let data = null
const CHANGE_EVENT = 'CHANGE_EVENT'

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
      return data
  }
})

PreviewsStore.dispatchToken = AppDispatcher.register(payload => {
  let action = payload.action
  switch (action.type) {
    case 'GOT_DATA':
      data = action.all
      PreviewsStore.emitChange()
      break;
  }
})

export default PreviewsStore
