import React from 'react';
import { connect } from 'react-redux';

import Modal from '../components/Modal';
import SavedSearchesList from '../components/SavedSearchesList';

import {
  deleteSavedSearch,
  closeSavedSearches
} from '../actions';

const SavedSearchesComponent = ({ display, close, savedSearches, onDelete }) => (
  <Modal isOpen={display}>
    <div className="header">
      Saved Searches
    </div>
    <div className="contents">
      {savedSearches.length === 0
        ? <p>No saved searches found</p>
        :
        <SavedSearchesList
          savedSearches={savedSearches}
          onDelete={onDelete}
        />
      }
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
  savedSearches: React.PropTypes.array,
  onDelete: React.PropTypes.func
};

const mapStateToProps = (state) => ({
  display: state.ui.showSavedSearches,
  savedSearches: (state.user.profile)
    ? state.user.profile.savedsearches
    : []
});

const mapDispatchToProps = (dispatch) => ({
  close: () => dispatch(closeSavedSearches()),
  onDelete: (e) => {
    dispatch(deleteSavedSearch(e));
  }
});

const SavedSearchesContainer = connect(
    mapStateToProps,
    mapDispatchToProps
)(SavedSearchesComponent);

export default SavedSearchesContainer;
