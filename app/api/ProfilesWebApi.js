import { AuthServiceFactory } from '../utils/AuthService';

const parseData = (resp) => JSON.parse(resp);

const checkStatus = (resp) => {
  if (resp.status === 200) return resp.text();

  return Promise.reject(new Error(resp.statusText));
};

export function updateProfile(searches) {
  const AuthService = AuthServiceFactory();
  const acceptJsonHeaders = {
    headers: {
      Accept: 'application/json',
      Authorization: `Bearer ${AuthService.getToken()}`,
      'Content-Type': 'application/json'
    },
    method: 'POST',
    cache: false,
    body: JSON.stringify(searches)
  };

  return fetch('/api/profiles/savedsearches', acceptJsonHeaders)
    .then(checkStatus)
    .then(parseData)
    .catch((err) => { throw new Error(err); });
}
