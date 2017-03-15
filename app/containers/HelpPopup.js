import { connect } from 'react-redux';

import HelpPopup from '../components/HelpPopup';
import { closeHelp } from '../actions';

export const mapStateToProps = (state) => ({
  display: state.ui.showHelp
});

export const mapDispatchToProps = (dispatch) => ({
  close: () => dispatch(closeHelp())
});

const HelpPopupContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(HelpPopup);

export default HelpPopupContainer;
