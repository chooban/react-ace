const acceptJsonHeaders = {
  headers: {
    Accept: 'application/json'
  }
};

function checkStatus(resp) {
  if (resp.status === 200) return resp.text();

  return Promise.reject(new Error(resp.statusText));
}

const parseData = (data) => JSON.parse(data);

export default function exportOrder(order) {
  const conf = {
    method: 'POST',
    headers: acceptJsonHeaders,
    cache: 'no-cache',
    body: order
  };

  return fetch('/api/orders/export', conf)
      .then(checkStatus)
      .then(parseData)
      .catch((err) => {
        throw new Error(err);
      });
}
