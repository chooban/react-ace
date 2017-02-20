import React from 'react';
import { connect } from 'react-redux';

import Modal from '../components/Modal';
import SavedSearchesList from '../containers/SavedSearchesListContainer';
import AddNewSavedSearch from './AddNewSavedSearchContainer';

import {
  closeSavedSearches
} from '../actions';

const SavedSearchesComponent = ({ display, close, hasSearches }) => (
  <Modal isOpen={display} width="400px" height="50%">
    <div className="header">
      Saved Searches
    </div>
    <div className="contents">
      {hasSearches
        ? <SavedSearchesList />
        : <p>No saved searches found</p>
      }
      <AddNewSavedSearch />
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
  hasSearches: React.PropTypes.bool
};

const mapStateToProps = (state) => ({
  display: state.ui.showSavedSearches,
  hasSearches: !!(state.user.profile && state.user.profile.savedsearches.length > 0)
});

const mapDispatchToProps = (dispatch) => ({
  close: () => dispatch(closeSavedSearches())
});

const SavedSearchesContainer = connect(
    mapStateToProps,
    mapDispatchToProps
)(SavedSearchesComponent);

export default SavedSearchesContainer;
