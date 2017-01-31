import React from 'react';
import { connect } from 'react-redux';

const ProfileIconComponent = () => (
  <div className="accounticon">
    <i
      className="material-icons"
    >
      person
    </i>
  </div>
);

ProfileIconComponent.propTypes = {
};

const ProfileIconContainer = connect()(ProfileIconComponent);

export default ProfileIconContainer;

