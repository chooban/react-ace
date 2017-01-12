import { connect } from 'react-redux';

import SearchComponent from '../components/Search';
import { updateSearch } from '../actions';

const mapDispatchToProps = (dispatch) => ({
  onSearchUpdate: (d) => requestAnimationFrame(dispatch.bind(this, updateSearch(d)))
});

const SearchContainer = connect(
  undefined,
  mapDispatchToProps
)(SearchComponent);

export default SearchContainer;
