import React from 'react';
import { connect } from 'react-redux';

import { showLogin } from '../actions/';

const LoginIconComponent = ({ display }) => (
  <div className="showlogin">
    <i
      className="material-icons"
      onClick={display}
    >
      person
    </i>
  </div>
);

LoginIconComponent.propTypes = {
  display: React.PropTypes.func
};

export const mapDispatchToProps = (dispatch) => ({
  display: () => dispatch(showLogin())
});

const LoginIconContainer = connect(
  null,
  mapDispatchToProps
)(LoginIconComponent);

export default LoginIconContainer;
