import React from 'react';
import IssueSelect from './containers/IssueSelectContainer';
import PreviewsGrid from './containers/PreviewsGridContainer';
import OrderView from './components/OrderView';

const App = () => (
  <div className="previewsApp">
    <div className="controlBar">
      <IssueSelect />
    </div>
    <PreviewsGrid />
    <OrderView />
  </div>
);

export default App;
