import React from 'react';
import { connect } from 'react-redux';

const LoginIconComponent = ({ authService }) => (
  <div className="accounticon">
    <i
      className="material-icons"
      onClick={() => authService.login()}
    >
      person_outline
    </i>
  </div>
);

LoginIconComponent.propTypes = {
  authService: React.PropTypes.object
};

const LoginIconContainer = connect()(LoginIconComponent);

export default LoginIconContainer;
