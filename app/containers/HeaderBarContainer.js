import { connect } from 'react-redux';

import HeaderBarComponent from '../components/HeaderBar';
import { AuthServiceFactory } from '../utils/AuthService';

const mapStateToProps = () => {
  const service = AuthServiceFactory();
  return {
    loggedIn: service.loggedIn()
  };
};

const HeaderBar = connect(mapStateToProps, null)(HeaderBarComponent);

export default HeaderBar;
