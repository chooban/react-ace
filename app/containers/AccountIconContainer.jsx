import React from 'react';
import { connect } from 'react-redux';

import ProfileIconContainer from './ProfileIcon';
import LoginIconContainer from './LoginIcon';

const AccountIconComponent = ({ isLoggedIn }) => {
  if (isLoggedIn) {
    return <ProfileIconContainer />;
  }
  return <LoginIconContainer />;
};

AccountIconComponent.propTypes = {
  isLoggedIn: React.PropTypes.bool.isRequired
};

const mapStateToProps = (state) => ({
  isLoggedIn: !!state.user.profile
});

const AccountIconContainer = connect(
  mapStateToProps,
  null
)(AccountIconComponent);

export default AccountIconContainer;
