import React from 'react'
import IssuePickerContainer from './IssuePickerContainer.jsx'
import OrderDetails from './OrderDetails.jsx'
import PreviewsGrid from './PreviewsGrid.jsx'

export default class App extends React.Component {
  constructor(props) {
    super(props)
  }

  render() {
    return(
      <div className="previewsApp">
        <div className="controlBar">
          <IssuePickerContainer/>
          <OrderDetails />
        </div>
        <PreviewsGrid />
      </div>
    )
  }

}
