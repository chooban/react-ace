import React from 'react';
import { connect } from 'react-redux';

import Modal from '../components/Modal';

import { closeSavedSearches } from '../actions';

const SavedSearchesComponent = ({ display, close, savedSearches }) => (
  <Modal isOpen={display}>
    <div className="header">
      Saved Searches
    </div>
    <div className="contents">
      <ul className="collection">
        {savedSearches.map((key, idx) => (
          <li
            className="collection-item"
            key={idx}
          >
            {key}
          </li>
          ))}
      </ul>
    </div>
    <div className="footer">
      <a
        tabIndex="-2"
        className="btn-flat"
        onClick={close}
      >
        Close
      </a>
    </div>
  </Modal>
);

SavedSearchesComponent.propTypes = {
  display: React.PropTypes.bool,
  close: React.PropTypes.func,
  savedSearches: React.PropTypes.array
};

const mapStateToProps = (state) => ({
  display: state.ui.showSavedSearches,
  savedSearches: (state.user.profile)
    ? state.user.profile.savedsearches
    : []
});

const mapDispatchToProps = (dispatch) => ({
  close: () => dispatch(closeSavedSearches())
});

const SavedSearchesContainer = connect(
    mapStateToProps,
    mapDispatchToProps
)(SavedSearchesComponent);

export default SavedSearchesContainer;
