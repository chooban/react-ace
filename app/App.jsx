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
  setUserProfile
} from './actions';

const service = AuthServiceFactory();

const AppComponent = ({ authService }) => (
  <div className="previewsApp">
    <nav>
      <div className="nav-wrapper">
        <SearchContainer />
        <OrderView />
        <HelpIconContainer />
        <AccountIconContainer authService={authService} />
      </div>
    </nav>
    <main className="content">
      <PreviewsGrid />
    </main>
    <OrderPopup />
    <ItemPreview />
    <HelpPopupContainer />
    <SavedSearchesContainer />
  </div>
);

AppComponent.propTypes = {
  authService: React.PropTypes.object
};

const mapDispatchToProps = (dispatch) => {
  service.onAuth((auth) => {
    auth.getProfile((err, profile) => {
      if (err) console.error(err); //eslint-disable-line

      dispatch(setUserProfile(profile));
    });
  });

  return {
    authService: service
  };
};

const App = connect(
  null,
  mapDispatchToProps
)(AppComponent);

export default App;
