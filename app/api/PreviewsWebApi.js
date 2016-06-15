const acceptJsonHeaders = {
  headers: {
    Accept: 'application/json'
  }
};

function checkStatus(resp) {
  if (resp.status === 200) return resp.text();

  return Promise.reject(new Error(resp.statusText));
}

export function getIssueList() {
  const parseData = (data) => JSON.parse(data);

  return fetch('/api/previews/', acceptJsonHeaders)
    .then(checkStatus)
    .then(parseData)
    .catch((err) => {
      throw new Error(err);
    });
}

export function getIssue(issueNumber) {
  const parseData = (resp) => JSON.parse(resp).contents;

  return fetch(`/api/previews/${issueNumber}`, acceptJsonHeaders)
    .then(checkStatus)
    .then(parseData)
    .catch((err) => {
      throw new Error(err);
    });
}
