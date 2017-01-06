import { connect } from 'react-redux';

import ToggleOrderComponent from '../components/ToggleOrder';

const mapStateToProps = (state, myProps) => ({
  ordered: myProps.ordered
});

const ToggleOrderContainer = connect(
  mapStateToProps
)(ToggleOrderComponent);

export default ToggleOrderContainer;
