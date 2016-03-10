import AppDispatcher from '../dispatcher/AppDispatcher'
import {GET_ISSUES, GOT_ISSUES, GET_ISSUE, GOT_ISSUE, CHANGED_ISSUE} from '../consts'
import d3 from 'd3'

export function getIssues() {
  AppDispatcher.handleAction({
    type: GET_ISSUES
  })

  gotIssues([
    { issue: 324 }
  , { issue: 326 }
  , { issue: 327 }
  ])
}

export function changedIssue(issueNumber) {
  AppDispatcher.handleAction({
    type: CHANGED_ISSUE
  , issue: issueNumber
  })

  d3.text(url(issueNumber), function(err, data) {
    if (err) return console.error(err)
    
    var parsedData = d3.csv.parseRows(data)
    gotIssueData(issueNumber, parsedData)
  })

  function url(issueNumber) {
    return 'data/ecmail' + issueNumber + '.csv'
  }
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
  , issue: issueNumber
  , issueData: issueData
  })
}
