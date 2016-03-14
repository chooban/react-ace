import Papa from 'BabyParse'

export function getIssueList(done) {
  done([
    { issue: 324 }
  , { issue: 326 }
  , { issue: 327 }
  , { issue: 330 }
  ])
}

export function getIssue(issueNumber, done) {
  fetch(url(issueNumber))
    .then(checkStatus)
    .then(parseData)
    .then((issueData) => {
      done(issueNumber, issueData)
    })
    .catch((err) => {
      console.error(err)
    })

  function url(issueNumber) {
    return 'data/ecmail' + issueNumber + '.csv'
  }

  function checkStatus(resp) {
    if (200 >= resp.status < 300) return resp.text()

    return Promise.reject(new Error(response.statusText))
  }

  function parseData(text) {
    var parsedData = Papa.parse(text)
    return parsedData.data
  }
}
