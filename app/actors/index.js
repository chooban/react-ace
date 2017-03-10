import {
  setUserProfile
} from '../actions';

import { AuthServiceFactory } from '../utils/AuthService';

const authService = AuthServiceFactory();
let profileFetchInFlight = false;

function setUserInfo(state, dispatch) {
  if (authService.loggedIn() && !state.user.profileFetched && !profileFetchInFlight) {
    profileFetchInFlight = true;
    authService.getProfile((err, profile) => {
      profileFetchInFlight = false;
      if (err) {
        console.error(err); //eslint-disable-line
      } else {
        dispatch(setUserProfile(profile));
      }
    });
  }
}

const actors = [
  setUserInfo
];

let acting = false;

export default (store) => {
  store.subscribe(() => {
    if (!acting) {
      acting = true;
      actors.forEach((a) => a(store.getState(), store.dispatch));
      acting = false;
    }
  });
};

