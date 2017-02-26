import { AuthServiceFactory } from '../utils/AuthService';

const AuthService = AuthServiceFactory();

const acceptJsonHeaders = {
  headers: {
    Accept: 'application/json',
    Authorization: `Bearer ${AuthService.getToken()}`
  },
  method: 'POST',
  cache: false
};

function checkStatus(resp) {
  if (resp.status === 200) return resp.text();

  return Promise.reject(new Error(resp.statusText));
}

export function updateProfile() {
  const parseData = (resp) => JSON.parse(resp);

  return fetch('/api/profiles/savedsearches', acceptJsonHeaders)
    .then(checkStatus)
    .then(parseData)
    .catch((err) => { throw new Error(err); });
}
