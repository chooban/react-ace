import React from 'react';

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
  onLogout: React.PropTypes.func.isRequired,
  displaySavedSearches: React.PropTypes.func.isRequired
};

export default ProfileIconComponent;
