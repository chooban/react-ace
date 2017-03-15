import React from 'react';

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

export default PreviewsItemViewComponent;
