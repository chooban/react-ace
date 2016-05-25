import React from 'react';
import IssueSelectContainer from './components/IssueSelectContainer.jsx';
import OrderDetails from './components/OrderDetails.jsx';
import PreviewsGrid from './components/PreviewsGrid.jsx';
import { getIssues } from './actions/PreviewsActions';

export default React.createClass({
  displayName: 'AceItApp',

  componentDidMount() {
    getIssues();
  },

  render() {
    return (
      <div className="previewsApp">
        <div className="controlBar">
          <IssueSelectContainer />
          <OrderDetails />
        </div>
        <PreviewsGrid/>
      </div>
    );
  },
});
