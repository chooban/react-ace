import React from 'react';

import OrderPopup from './containers/OrderPopupContainer';
import ItemPreview from './containers/PreviewsItemViewContainer';
import PreviewsGrid from './containers/PreviewsGridContainer';
import OrderView from './containers/ShoppingCartContainer';
import SearchContainer from './containers/SearchContainer';

const App = () => (
  <div className="previewsApp">
    <nav>
      <div className="nav-wrapper">
        <SearchContainer />
        <OrderView />
      </div>
    </nav>
    <main className="content">
      <PreviewsGrid />
    </main>
    <OrderPopup />
    <ItemPreview />
  </div>
);

export default App;
