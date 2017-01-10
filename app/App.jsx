import React from 'react';

import OrderPopup from './containers/OrderPopupContainer';
import PreviewsGrid from './containers/PreviewsGridContainer';
import OrderView from './containers/OrderSummaryContainer';
import SearchContainer from './containers/SearchContainer';

const App = () => (
  <div className="previewsApp">
    <div className="appheader">
      <div className="content">
        <img role="presentation" src="ace-comics-logo-header.svg" />
        <SearchContainer />
        <OrderView />
      </div>
    </div>
    <div className="appcontent">
      <div className="content">
        <PreviewsGrid />
      </div>
    </div>
    <OrderPopup />
  </div>
);

export default App;
