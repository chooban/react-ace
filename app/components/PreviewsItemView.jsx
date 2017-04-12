import React from 'react';
import PropTypes from 'prop-types';

import Modal from './Modal';
import ItemPreview from './PreviewsItemPreview';
import ToggleOrder from '../containers/ToggleOrderContainer';

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
        className="btn blue-grey lighten-3"
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
  display: PropTypes.bool,
  close: PropTypes.func.isRequired,
  previewsCode: PropTypes.string
};

PreviewsItemViewComponent.defaultProps = {
  display: false,
  previewsCode: ''
};

export default PreviewsItemViewComponent;
