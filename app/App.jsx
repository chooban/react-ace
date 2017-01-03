import React from 'react';
import OrderPopup from './containers/OrderPopupContainer';
import PreviewsGrid from './containers/PreviewsGridContainer';
import OrderView from './containers/OrderViewContainer';

const App = () => (
  <div className="previewsApp">
    <OrderView />
    <PreviewsGrid />
    <OrderPopup />
  </div>
);

export default App;
