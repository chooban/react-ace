import React from 'react';
import PreviewsGrid from './containers/PreviewsGridContainer';
import OrderView from './components/OrderView';

const App = () => (
  <div className="previewsApp">
    <OrderView />
    <PreviewsGrid />
  </div>
);

export default App;
