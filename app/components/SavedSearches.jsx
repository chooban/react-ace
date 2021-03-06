import React from 'react';
import PropTypes from 'prop-types';

import Modal from './Modal';
import SavedSearchesList from '../containers/SavedSearchesListContainer';
import AddNewSavedSearch from '../containers/AddNewSavedSearchContainer';

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
        className="btn"
        onClick={close}
      >
        Close
      </a>
    </div>
  </Modal>
);

SavedSearchesComponent.propTypes = {
  display: PropTypes.bool,
  close: PropTypes.func.isRequired,
  hasSearches: PropTypes.bool
};

SavedSearchesComponent.defaultProps = {
  display: false,
  hasSearches: false
};

export default SavedSearchesComponent;
