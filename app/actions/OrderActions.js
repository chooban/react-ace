import {ADD_TO_ORDER, REMOVE_FROM_ORDER} from '../consts'
import AppDispatcher from '../dispatcher/AppDispatcher'

export function addToOrder(previewsCode) {
  AppDispatcher.handleAction({
      type: ADD_TO_ORDER
    , previewsCode: previewsCode
  })
}

export function removeFromOrder(previewsCode) {
  AppDispatcher.handleAction({
      type: REMOVE_FROM_ORDER
    , previewsCode: previewsCode
  })
}
