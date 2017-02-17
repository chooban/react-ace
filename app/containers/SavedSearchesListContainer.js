import { connect } from 'react-redux';

import SavedSearchesList from '../components/SavedSearchesList';

import {
  deleteSavedSearch,
  performSavedSearch
} from '../actions';

const mapStateToProps = (state) => ({
  savedSearches: (state.user.profile)
    ? state.user.profile.savedsearches.sort()
    : []
});

const mapDispatchToProps = (dispatch) => ({
  onDelete: (key) => {
    dispatch(deleteSavedSearch(key));
  },
  onSelect: (key) => {
    dispatch(performSavedSearch(key));
  }
});

const SavedSearchesListContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(SavedSearchesList);

export default SavedSearchesListContainer;
