const acceptJsonHeaders = {
  headers: {
    Accept: 'application/json'
  }
};

function checkStatus(resp) {
  if (resp.status === 200) return resp.text();

  return Promise.reject(new Error(resp.statusText));
}

export function getLatestIssue() {
  const parseData = (resp) => JSON.parse(resp);

  return fetch('/api/previews/latest', acceptJsonHeaders)
    .then(checkStatus)
    .then(parseData)
    .catch((err) => { throw new Error(err); });
}
