import React from 'react';
import { connect } from 'react-redux';
import {
  logout as logoutAction
} from '../actions/';

const ProfileIconComponent = ({ authService, doLogout }) => (
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
  authService: React.PropTypes.object,
  doLogout: React.PropTypes.func
};

const mapDispatchToProps = (dispatch) => ({
  doLogout: (authService) => {
    authService.logout();
    dispatch(logoutAction());
  }
});

const ProfileIconContainer = connect(
  null,
  mapDispatchToProps
)(ProfileIconComponent);

export default ProfileIconContainer;

