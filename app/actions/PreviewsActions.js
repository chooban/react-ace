import AppDispatcher from '../dispatcher/AppDispatcher'
import {GET_ISSUES, GOT_ISSUES, GOT_ISSUE, CHANGED_ISSUE} from '../consts'
import {getIssueList, getIssue} from '../api/PreviewsWebApi'

export function getIssues() {
  AppDispatcher.handleAction({
    type: GET_ISSUES
  })

  getIssueList(gotIssues)
}

export function changedIssue(issueNumber) {
  AppDispatcher.handleAction({
    type: CHANGED_ISSUE
  , issueNumber: issueNumber
  })

  getIssue(issueNumber, gotIssueData)
}

function gotIssues(data) {
  AppDispatcher.handleAction({
      type: GOT_ISSUES
    , all: data
  })
}

function gotIssueData(issueNumber, issueData) {
  AppDispatcher.handleAction({
    type: GOT_ISSUE
  , issueNumber: issueNumber
  , issueData: issueData
  })
}
