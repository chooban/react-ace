import { connect } from 'react-redux';

import SearchComponent from '../components/Search';
import { updateSearch } from '../actions';

export const mapStateToProps = (state) => ({
  searchValue: state.gridConfig.searchTerm
});

export const mapDispatchToProps = (dispatch) => ({
  onSearchUpdate: (d) => dispatch(updateSearch(d))
});

const SearchContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(SearchComponent);

export default SearchContainer;
