import React from 'react';
import PropTypes from 'prop-types';

import ProfileIconContainer from '../containers/ProfileIcon';
import LoginIconContainer from '../containers/LoginIcon';

const AccountIconComponent = ({ isLoggedIn }) => {
  if (isLoggedIn) {
    return <ProfileIconContainer />;
  }
  return <LoginIconContainer />;
};

AccountIconComponent.propTypes = {
  isLoggedIn: PropTypes.bool.isRequired
};

export default AccountIconComponent;
