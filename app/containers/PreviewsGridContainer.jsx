import { connect } from 'react-redux';
import PreviewsGrid from '../components/PreviewsGrid';

const props = {
  gridData: [],
  searchableProperties: ['title', 'publisher'],
  onItemSelected: (d) => console.log(d) //eslint-disable-line
};

const mapStateToProps = (state) => (
  Object.assign({}, props, {
    gridData: state.issues.data
  })
);

const mapDispatchToProps = () => ({});

const PreviewsGridContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(PreviewsGrid);

export default PreviewsGridContainer;
