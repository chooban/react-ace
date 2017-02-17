import { connect } from 'react-redux';

import ClickableIcon from '../components/ClickableIcon';
import { showHelp } from '../actions/';

export const mapStateToProps = () => ({
  className: 'showhelp',
  iconName: 'help'
});

export const mapDispatchToProps = (dispatch) => ({
  onClick: () => dispatch(showHelp())
});

const HelpIconContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(ClickableIcon);

export default HelpIconContainer;
