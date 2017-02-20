import { connect } from 'react-redux';

import SavedSearchesList from '../components/SavedSearchesList';

import {
  deleteSavedSearch,
  performSavedSearch
} from '../actions';

import {
  hitCountForSearch
} from '../utils/CatalogueSearch';

const getHitCounts = (searchTerms, catalogue) => (
  searchTerms.map((term) => ({
    searchTerm: term,
    hits: hitCountForSearch(term, catalogue)
  })
));

export const mapStateToProps = (state) => ({
  savedSearches: (state.user.profile)
    ? getHitCounts(
        state.user.profile.savedsearches.sort(),
        state.issues.data
      )
    : []
});

export const mapDispatchToProps = (dispatch) => ({
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
