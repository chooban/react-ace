import AppDispatcher from '../dispatcher/AppDispatcher'
import {GET_ISSUES, GOT_ISSUES, GET_ISSUE, GOT_ISSUE} from '../consts'
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

export function getIssue(issueNumber) {
  AppDispatcher.handleAction({
    type: GET_ISSUE
  })

  d3.text('data/ecmail324.csv', function(err, data) {
    if (err) { console.error(err)
    }
    else {
      var parsedData = d3.csv.parseRows(data)
      gotIssueData(issueNumber, parsedData)
    }
  })
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
