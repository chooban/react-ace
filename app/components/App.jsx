import React from 'react'
import IssueSelectContainer from './IssueSelectContainer.jsx'
import OrderDetails from './OrderDetails.jsx'
import PreviewsGrid from './PreviewsGrid.jsx'

export default React.createClass({
    displayName: "AceItApp"
  , render() {
      return(
        <div className="previewsApp">
          <div className="controlBar">
            <IssueSelectContainer />
            <OrderDetails />
          </div>
          <PreviewsGrid/>
        </div>
      )
    }
})
