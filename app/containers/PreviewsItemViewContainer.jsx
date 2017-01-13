import React from 'react';
import { connect } from 'react-redux';

import { closePreview } from '../actions';
import Modal from '../components/Modal';
import ItemPreview from '../components/PreviewsItemPreview';

const PreviewsItemViewComponent = ({ display, close, previewsCode }) => (
  <Modal isOpen={display}>
    <div className="header">
      Previews Preview
    </div>
    <div className="contents">
      <ItemPreview previewsCode={previewsCode} />
    </div>
    <div className="footer">
      <a
        tabIndex="-2"
        className="btn-flat"
        onClick={close}
      >
        Close
      </a>
      <a
        tabIndex="-1"
        className="btn-flat"
      >
        Add To Order
      </a>
    </div>
  </Modal>
);

PreviewsItemViewComponent.propTypes = {
  display: React.PropTypes.bool,
  close: React.PropTypes.func,
  previewsCode: React.PropTypes.string
};

const mapStateToProps = (state) => ({
  display: state.ui.showItemPreview,
  previewsCode: state.ui.itemPreview
});

const PreviewsItemViewContainer = connect(
  mapStateToProps,
  {
    close: () => (dispatch) => dispatch(closePreview())
  }
)(PreviewsItemViewComponent);

export default PreviewsItemViewContainer;
