import React from 'react';
import { connect } from 'react-redux';

import { showHelp } from '../actions/';

const HelpIconComponent = ({ display }) => (
  <div className="showhelp">
    <i
      className="material-icons"
      onClick={display}
    >
      help
    </i>
  </div>
);

HelpIconComponent.propTypes = {
  display: React.PropTypes.func
};

const mapDispatchToProps = (dispatch) => ({
  display: () => dispatch(showHelp())
});

const HelpIconContainer = connect(
  null,
  mapDispatchToProps
)(HelpIconComponent);

export default HelpIconContainer;
