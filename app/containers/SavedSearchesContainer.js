import { connect } from 'react-redux';

import SavedSearchesComponent from '../components/SavedSearches';
import { closeSavedSearches } from '../actions';

export const mapStateToProps = (state) => ({
  display: state.ui.showSavedSearches,
  hasSearches: !!(state.user.profile && state.user.profile.savedsearches.length > 0)
});

export const mapDispatchToProps = (dispatch) => ({
  close: () => dispatch(closeSavedSearches())
});

const SavedSearchesContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(SavedSearchesComponent);

export default SavedSearchesContainer;
