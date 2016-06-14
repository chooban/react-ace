import React from 'react';
import IssueSelect from './containers/IssueSelectContainer.jsx';
import PreviewsGrid from './containers/PreviewsGridContainer.jsx';

const App = () => (
  <div className="previewsApp">
    <div className="controlBar">
      <IssueSelect />
    </div>
    <PreviewsGrid />
  </div>
);

export default App;
