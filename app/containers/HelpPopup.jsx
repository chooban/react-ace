import React from 'react';
import { connect } from 'react-redux';

import { closeHelp } from '../actions';
import Modal from '../components/Modal';

const HelpComponent = ({ display, close }) => (
  <Modal isOpen={display}>
    <div className="header">
      Help
    </div>
    <div className="contents">
      <p>
        Add the items you want to the cart, export your order,
        and then email to Ace. Simple!
      </p>

      <p>
        If for some reason it&apos;s not working,
        you can <a href="/api/previews/latest.csv">download the CSV file</a> instead.
      </p>

      <p>
        Bug reports are always welcome,
        just <a href="mailto:rhendry@googlemail.com">drop me an email</a>.
      </p>
    </div>
    <div className="footer">
      <a
        tabIndex="-1"
        className="btn-flat"
        onClick={close}
      >
        Close
      </a>
    </div>
  </Modal>
);

HelpComponent.propTypes = {
  display: React.PropTypes.bool.isRequired,
  close: React.PropTypes.func.isRequired
};

const mapStateToProps = (state) => ({
  display: state.ui.showHelp
});

const HelpPopupContainer = connect(
  mapStateToProps,
  {
    close: () => (dispatch) => dispatch(closeHelp())
  }
)(HelpComponent);

export default HelpPopupContainer;
