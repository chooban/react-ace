import {Dispatcher} from 'flux'
import assign from 'object-assign'

export default assign(new Dispatcher(), {
  handleAction(action) {
    console.log(JSON.stringify(action))
    this.dispatch({
      action: action
    })
  }
})
