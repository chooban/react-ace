const acceptJsonHeaders = {
  headers: {
    Accept: 'application/json'
  }
};

function checkStatus(resp) {
  if (resp.status === 200) return resp.text();

  return Promise.reject(new Error(resp.statusText));
}

export default function () {
  const parseData = (resp) => JSON.parse(resp);

  return fetch('/api/bootstrap/', acceptJsonHeaders)
    .then(checkStatus)
    .then(parseData)
    .then((parsedData) => {
      localStorage.setItem('auth0_id', parsedData.clientId);
      localStorage.setItem('auth0_domain', parsedData.domain);
    })
    .catch((err) => { throw new Error(err); });
}
