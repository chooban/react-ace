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
  var resultHandler = gotIssueData.bind(this, issueNumber)
  console.log("Pre action")
  AppDispatcher.handleAction({
    type: GET_ISSUE
  })
  console.log("Post action")

  d3.csv('data/ecmail324.csv', function(err, data) {
    console.log("Got data")
    if(err) console.error(err)
    else resultHandler(data)
  })
}

function gotIssues(data) {
  AppDispatcher.handleAction({
      type: GOT_ISSUES
    , all: data
  })
}

function gotIssueData(issueNumber, issueData) {
  console.log(arguments)
  AppDispatcher.handleAction({
    type: GOT_ISSUE
  , issue: issueNumber
  , issueData: issueData
  })
}
