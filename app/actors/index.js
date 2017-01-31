import {
  requestIssue,
  setUserProfile
} from '../actions';

import { AuthServiceFactory } from '../utils/AuthService';

const authService = AuthServiceFactory();

function fetchInitialGridData(state, dispatch) {
  if (state.issues.issuesList.length && !state.issues.data.length) {
    dispatch(requestIssue(state.issues.issuesList[0]));
  }
}

function setUserInfo(state, dispatch) {
  if (authService.loggedIn() && !state.user.profile) {
    authService.getProfile((err, profile) => {
      if (err) console.error(err); //eslint-disable-line

      dispatch(setUserProfile(profile));
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

