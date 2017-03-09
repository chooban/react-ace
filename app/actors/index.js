import {
  requestIssue,
  setUserProfile
} from '../actions';

import { AuthServiceFactory } from '../utils/AuthService';

const authService = AuthServiceFactory();
let profileFetchInFlight = false;

function fetchInitialGridData(state, dispatch) {
  if (state.issues.issuesList.length && !state.issues.data.length) {
    dispatch(requestIssue(state.issues.issuesList[0]));
  }
}

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
  fetchInitialGridData,
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

