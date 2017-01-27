import React from 'react';
import { connect } from 'react-redux';
import Auth0Lock from 'auth0-lock';

const LockComponent = ({ display, lock }) => {
  if (!display) return null;

  lock.show();
  return '';
};

LockComponent.propTypes = {
  display: React.PropTypes.bool.isRequired,
  lock: React.PropTypes.object
};

const mapStateToProps = (state) => ({
  display: state.ui.showLogin,
  lock: new Auth0Lock(
      '3ZRxcpSCqh6CnKU1zFZuWbKY0uIrfK7D',
      'acemyorder.eu.auth0.com'
      )
});

const LockContainer = connect(
    mapStateToProps
)(LockComponent);

export default LockContainer;
