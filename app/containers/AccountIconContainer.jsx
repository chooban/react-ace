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

const AccountIconContainer = connect()(AccountIconComponent);

export default AccountIconContainer;
