export function getIssueList(done) {
  //done([
    //{ issue: 324 }, { issue: 326 }, { issue: 327 }, { issue: 330 },
  //]);
  fetch('api/previews/')
    .then(checkStatus)
    .then((data) => data(null, data))
    .catch((err) => {
      console.error(err);
      done(err);
    });
}

export function getIssue(issueNumber, done) {
  fetch(url(issueNumber))
    .then(checkStatus)
    .then(parseData)
    .then((issueData) => {
      done(null, issueNumber, issueData);
    })
    .catch((err) => {
      console.error(err);
      done(err);
    });

  function url(issueNumber) {
    return 'data/ecmail' + issueNumber + '.csv';
  }

  function parseData(resp) {
    return resp.body;
  }
}

function checkStatus(resp) {
  if (200 >= resp.status < 300) return resp.text();

  return Promise.reject(new Error(response.statusText));
}
