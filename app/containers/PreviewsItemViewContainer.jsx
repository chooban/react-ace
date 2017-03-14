import React from 'react';
import { connect } from 'react-redux';

import {
  closePreview
} from '../actions';

import Modal from '../components/Modal';
import ItemPreview from '../components/PreviewsItemPreview';
import ToggleOrder from './ToggleOrderContainer';

const PreviewsItemViewComponent = ({ display, previewsCode, close }) => (
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
      <ToggleOrder
        previewsCode={previewsCode}
        type="button"
      />
    </div>
  </Modal>
);

PreviewsItemViewComponent.propTypes = {
  display: React.PropTypes.bool,
  close: React.PropTypes.func.isRequired,
  previewsCode: React.PropTypes.string
};

PreviewsItemViewComponent.defaultProps = {
  display: false,
  previewsCode: ''
};

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
