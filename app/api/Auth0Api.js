import { AuthServiceFactory } from './utils/AuthService';

const acceptJsonHeaders = {
  headers: {
    Accept: 'application/json'
  },
  method: 'PATCH'
};

export function updateProfileMetadata(profile) {
  const service = AuthServiceFactory();

  return fetch(`https:\\${AuthServiceFactory.url}/api/v2/users)
}
