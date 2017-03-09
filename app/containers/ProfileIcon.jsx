import React from 'react';
import { connect } from 'react-redux';
import {
  logout as logoutAction,
  showSavedSearches
} from '../actions/';
import { AuthServiceFactory } from '../utils/AuthService';

const ProfileIconComponent = ({ authService, doLogout, displaySavedSearches }) => (
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
        onClick={() => doLogout(authService)}
      >
        Logout
      </a>
    </div>
  </div>
);

ProfileIconComponent.propTypes = {
  authService: React.PropTypes.object.isRequired,
  doLogout: React.PropTypes.func.isRequired,
  displaySavedSearches: React.PropTypes.func.isRequired
};

const mapStateToProps = () => ({
  authService: AuthServiceFactory()
});

const mapDispatchToProps = (dispatch) => ({
  displaySavedSearches: () => dispatch(showSavedSearches()),
  doLogout: (authService) => {
    authService.logout();
    dispatch(logoutAction());
  }
});

const ProfileIconContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(ProfileIconComponent);

export default ProfileIconContainer;

