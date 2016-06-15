import { connect } from 'react-redux';
import { addToOrder } from '../actions';
import PreviewsGrid from '../components/PreviewsGrid';

const props = {
  gridData: [],
  searchableProperties: ['title', 'publisher']
};

const mapStateToProps = (state) => (
  Object.assign({}, props, {
    gridData: state.issues.data
  })
);

const mapDispatchToProps = (dispatch) => (
  {
    onItemSelected: (d) => dispatch(addToOrder(d))
  }
);

const PreviewsGridContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(PreviewsGrid);

export default PreviewsGridContainer;
