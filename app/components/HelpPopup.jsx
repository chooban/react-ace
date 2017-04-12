import React from 'react';
import PropTypes from 'prop-types';

import Modal from './Modal';

const HelpPopup = ({ display, close }) => (
  <Modal isOpen={display}>
    <div className="header">
      Help
    </div>
    <div className="contents">
      <p>
        Add the items you want to the cart, export your order,
        and then email to Ace. Simple! If you want to be able to save searches
        so that you can run them every month and stop missing books (or is that
        just me) then create an account.
      </p>

      <p>
        If for some reason it&apos;s not working,
        you can <a href="/api/previews/latest.csv">download the CSV file</a>
        .
      </p>

      <p>
        Bug reports are always welcome,
        just <a href="mailto:rhendry@googlemail.com">drop me an email</a>
        .
      </p>
    </div>
    <div className="footer">
      <a
        tabIndex="-1"
        className="btn blue-grey lighten-3"
        onClick={close}
      >
        Close
      </a>
    </div>
  </Modal>
);

HelpPopup.propTypes = {
  display: PropTypes.bool.isRequired,
  close: PropTypes.func.isRequired
};

export default HelpPopup;
