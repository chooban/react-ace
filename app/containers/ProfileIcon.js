import { connect } from 'react-redux';

import ProfileIconComponent from '../components/ProfileIcon';
import { AuthServiceFactory } from '../utils/AuthService';
import {
  logout as logoutAction,
  showSavedSearches
} from '../actions/';

export const mapDispatchToProps = (dispatch) => {
  const authService = AuthServiceFactory();
  return {
    displaySavedSearches: () => dispatch(showSavedSearches()),
    onLogout: () => {
      authService.logout();
      dispatch(logoutAction());
    }
  };
};

const ProfileIconContainer = connect(
  null,
  mapDispatchToProps
)(ProfileIconComponent);

export default ProfileIconContainer;

