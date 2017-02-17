import { connect } from 'react-redux';

import ClickableIcon from '../components/ClickableIcon';
import { AuthServiceFactory } from '../utils/AuthService';

const authService = AuthServiceFactory();

const mapStateToProps = () => ({
  className: 'accounticon',
  iconName: 'person_outline',
  onClick: authService.login
});

const LoginIconContainer = connect(
  mapStateToProps
)(ClickableIcon);

export default LoginIconContainer;
