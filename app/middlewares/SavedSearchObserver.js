import { AuthServiceFactory } from '../utils/AuthService';
import { updateProfile } from '../api/ProfilesWebApi';
import { setUserProfile } from '../actions';
import debounce from '../utils/debounce';

const authService = AuthServiceFactory();
let cb;

export default (store) => (next) => (action) => {
  const uploadSavedSearches = () => {
    const searches = store.getState().user.profile.savedsearches;

    updateProfile(searches)
      .then(() => {
        authService.getProfile((err, profile) => {
          if (err) {
            //eslint-disable-next-line
            console.error('Error fetching profile');

            //eslint-disable-next-line
            console.error(err);
          }
          store.dispatch(setUserProfile(profile));
        });
      })
      .then(() => { cb = null; })
      .catch(() => { cb = null; });
  };
  if (!cb) cb = debounce(uploadSavedSearches, 2000);

  const result = next(action);

  if (action.type === 'ADD_SAVED_SEARCH' || action.type === 'DELETE_SAVED_SEARCH') {
    cb();
  }
  return result;
};
