import { connect } from 'react-redux';

import { addSavedSearch } from '../actions';
import AddNewSavedSearchComponent from '../components/AddNewSavedSearch';

export const mapDispatchToProps = (dispatch) => ({
  onAdd: (newSearch) => dispatch(addSavedSearch(newSearch))
});

const AddNewSavedSearch = connect(
  null,
  mapDispatchToProps
)(AddNewSavedSearchComponent);

export default AddNewSavedSearch;
