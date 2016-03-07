import AppDispatcher from '../dispatcher/AppDispatcher'
import {CHOSE_ISSUE} from '../consts'

export function choseIssue(issue) {
  AppDispatcher.handleAction({
    type: CHOSE_ISSUE
  , issue: issue
  })
}
