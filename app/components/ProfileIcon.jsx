import React from 'react';
import PropTypes from 'prop-types';

const ProfileIconComponent = ({ onLogout, displaySavedSearches }) => (
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
        onClick={() => onLogout()}
      >
        Logout
      </a>
    </div>
  </div>
);

ProfileIconComponent.propTypes = {
  onLogout: PropTypes.func.isRequired,
  displaySavedSearches: PropTypes.func.isRequired
};

export default ProfileIconComponent;
