import React from 'react';
import { connect } from 'react-redux';

import ProfileIconContainer from './ProfileIcon';
import LoginIconContainer from './LoginIcon';

const AccountIconComponent = ({ isLoggedIn, authService }) => {
  if (isLoggedIn) {
    return <ProfileIconContainer authService={authService} />;
  }
  return <LoginIconContainer authService={authService} />;
};

AccountIconComponent.propTypes = {
  isLoggedIn: React.PropTypes.bool.isRequired,
  authService: React.PropTypes.object.isRequired
};

const mapStateToProps = (state) => ({
  isLoggedIn: !!state.user.profile
});

const AccountIconContainer = connect(
  mapStateToProps,
  null
)(AccountIconComponent);

export default AccountIconContainer;
