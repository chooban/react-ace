import React from 'react';

import OrderPopup from './containers/OrderPopupContainer';
import PreviewsGrid from './containers/PreviewsGridContainer';
import OrderView from './containers/OrderSummaryContainer';
import SearchContainer from './containers/SearchContainer';

const App = () => (
  <div className="previewsApp">
    <nav>
      <div className="nav-wrapper">
        <SearchContainer />
        <OrderView />
      </div>
    </nav>
    <div className="appcontent">
      <div className="content">
        <PreviewsGrid />
      </div>
    </div>
    <OrderPopup />
  </div>
);

export default App;
