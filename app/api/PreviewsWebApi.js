export function getIssueList() {
  return fetch('/api/previews/', {
      headers: {
        'Accept': 'application/json',
      }
    })
    .then(checkStatus)
    .then(parseData)
    .catch((err) => {
      console.error(err);
      throw new Error(err);
    });

  function parseData(data) {
    return JSON.parse(data);
  }
}

export function getIssue(issueNumber) {
  return fetch(url(issueNumber), {
      headers: {
        'Accept': 'application/json',
      }
    })
    .then(checkStatus)
    .then(parseData)
    .catch((err) => {
      console.error(err);
      throw new Error(err);
    });

  function url(issueNumber) {
    return '/api/previews/' + issueNumber;
  }

  function parseData(resp) {
    const parsedResponse = JSON.parse(resp);
    return parsedResponse.contents;
  }
}

function checkStatus(resp) {
  if (200 >= resp.status < 300) return resp.text();

  return Promise.reject(new Error(response.statusText));
}
