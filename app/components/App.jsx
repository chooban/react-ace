import React from 'react'
import IssuePickerContainer from './IssuePickerContainer.jsx'
import OrderDetails from './OrderDetails.jsx'
import PreviewsGridContainer from './PreviewsGridContainer.jsx'

export default React.createClass({
    displayName: "AceItApp"
  , getInitialState() {
      return {
        selectedIssue: null
      }
    }
  , render() {
      return(
        <div className="previewsApp">
          <div className="controlBar">
            <IssuePickerContainer doneSelectIssue={this.handleIssueSelected} />
            <OrderDetails />
          </div>
          <PreviewsGridContainer selectedIssue={this.state.selectedIssue}/>
        </div>
      )
    }
  , handleIssueSelected(selectedIssue) {
      this.setState({
        selectedIssue: selectedIssue
      })
    }
})
