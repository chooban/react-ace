import React from 'react';
import { connect } from 'react-redux';

import OrderPopup from './containers/OrderPopupContainer';
import ItemPreview from './containers/PreviewsItemViewContainer';
import PreviewsGrid from './containers/PreviewsGridContainer';
import OrderView from './containers/ShoppingCartContainer';
import SearchContainer from './containers/SearchContainer';
import HelpIconContainer from './containers/HelpIcon';
import HelpPopupContainer from './containers/HelpPopup';
import AccountIconContainer from './containers/AccountIconContainer';
import SavedSearchesContainer from './containers/SavedSearchesContainer';

import { AuthServiceFactory } from './utils/AuthService';
import {
  logout,
  setUserProfile
} from './actions';


const AppComponent = ({ loggedIn }) => (
  <div className="previewsApp">
    <nav>
      <div className="nav-wrapper">
        <SearchContainer />
        <OrderView />
        <HelpIconContainer />
        <AccountIconContainer isLoggedIn={loggedIn} />
      </div>
    </nav>
    <main className="content">
      <PreviewsGrid />
      <OrderPopup />
      <ItemPreview />
      <HelpPopupContainer />
      <SavedSearchesContainer />
    </main>
  </div>
);

AppComponent.propTypes = {
  loggedIn: React.PropTypes.bool.isRequired
};

const mapStateToProps = () => {
  const service = AuthServiceFactory();
  return {
    loggedIn: service.loggedIn()
  };
};

const mapDispatchToProps = (dispatch) => {
  const service = AuthServiceFactory();
  service.onAuth((auth) => {
    auth.getProfile((err, profile) => {
      if (err) {
        //eslint-disable-next-line
        console.error(err);
        dispatch(logout());
      }

      dispatch(setUserProfile(profile));
    });
  });

  return {};
};

const App = connect(
  mapStateToProps,
  mapDispatchToProps
)(AppComponent);

export default App;
