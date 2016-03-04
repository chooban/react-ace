import AppDispatcher from '../dispatcher/AppDispatcher'
import {GET_DATA, GOT_DATA} from '../consts'

export function getData() {
  AppDispatcher.handleViewAction({
    type: GET_DATA
  })

  gotData([
    { issue: 324 }
  , { issue: 325 }
  , { issue: 326 }
  ])
}

export function gotData(data) {
  AppDispatcher.handleServerAction({
      type: GOT_DATA
    , all: data
  })
}
