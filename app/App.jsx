import React from 'react';
import { connect } from 'react-redux';

import Reboot from 'material-ui/Reboot';
import { withStyles } from 'material-ui/styles';

import HeaderBarContainer from './containers/HeaderBarContainer';
import OrderPopup from './containers/OrderPopupContainer';
import ItemPreview from './containers/PreviewsItemViewContainer';
import PreviewsGrid from './containers/PreviewsGridContainer';
import HelpPopupContainer from './containers/HelpPopup';
import SavedSearchesContainer from './containers/SavedSearchesContainer';

import { AuthServiceFactory } from './utils/AuthService';
import {
  logout,
  setUserProfile
} from './actions';

/*
 *
            <SearchContainer />
            <OrderView />
            <HelpIconContainer />
            <AccountIconComponent isLoggedIn={loggedIn} />
 */

const AppComponent = () => (
  <div className="previewsApp">
    <Reboot />
    <header>
      <nav>
        <div className="nav-wrapper container">
          <HeaderBarContainer />
        </div>
      </nav>
    </header>
    <main className="content container">
      <PreviewsGrid />
      <OrderPopup />
      <ItemPreview />
      <HelpPopupContainer />
      <SavedSearchesContainer />
    </main>
  </div>
);

const mapDispatchToProps = (dispatch) => {
  const service = AuthServiceFactory();
  service.onAuth((auth) => {
    auth.getProfile((err, profile) => {
      if (err) {
        // eslint-disable-next-line
        console.error(err);
        dispatch(logout());
      }

      dispatch(setUserProfile(profile));
    });
  });

  return {};
};

const App = connect(
  null,
  mapDispatchToProps
)(AppComponent);

export default withStyles({})(App);
