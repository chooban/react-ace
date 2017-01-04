import React from 'react';
import OrderPopup from './containers/OrderPopupContainer';
import PreviewsGrid from './containers/PreviewsGridContainer';
import OrderView from './containers/OrderSummaryContainer';

const App = () => (
  <div className="previewsApp">
    <div className="appheader">
      <div className="content">
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
