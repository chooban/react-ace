import { connect } from 'react-redux';
import PreviewsGrid from '../components/PreviewsGrid';

const props = {
  gridData: [],
  searchableProperties: ['title', 'publisher']
}

const mapStateToProps = (state) => {
  return Object.assign({}, props, {
    gridData: state.issues.data
  });
}

const mapDispatchToProps = (dispatch) => {
  return {};
}

const PreviewsGridContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(PreviewsGrid);

export default PreviewsGridContainer;
