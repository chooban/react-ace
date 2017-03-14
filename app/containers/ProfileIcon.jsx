import React from 'react';
import { connect } from 'react-redux';

import { AuthServiceFactory } from '../utils/AuthService';
import {
  logout as logoutAction,
  showSavedSearches
} from '../actions/';

const ProfileIconComponent = ({ onLogout, displaySavedSearches }) => (
  <div className="accounticon">
    <i
      className="material-icons"
    >
      person
    </i>
    <div className="submenu collection">
      <a
        href="#!"
        className="collection-item"
        onClick={displaySavedSearches}
      >
        Saved Searches
      </a>
      <a
        href="#!"
        className="collection-item"
        onClick={() => onLogout()}
      >
        Logout
      </a>
    </div>
  </div>
);

ProfileIconComponent.propTypes = {
  onLogout: React.PropTypes.func.isRequired,
  displaySavedSearches: React.PropTypes.func.isRequired
};

export const mapDispatchToProps = (dispatch) => {
  const authService = AuthServiceFactory();
  return {
    displaySavedSearches: () => dispatch(showSavedSearches()),
    doLogout: () => {
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

