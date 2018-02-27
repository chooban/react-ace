import { connect } from 'react-redux';

import PreviewsItemViewComponent from '../components/PreviewsItemView';
import { closePreview } from '../actions';

export const mapStateToProps = (state) => ({
  display: state.ui.showItemPreview,
  previewsCode: state.ui.itemPreview
});

export const mapDispatchToProps = (dispatch) => ({
  close: () => dispatch(closePreview())
});

const PreviewsItemViewContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(PreviewsItemViewComponent);

export default PreviewsItemViewContainer;
