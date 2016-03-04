import React from 'react'
import IssuePickerContainer from './IssuePickerContainer.jsx'
import OrderDetails from './OrderDetails.jsx'
import PreviewsGrid from './PreviewsGrid.jsx'

export default class App extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
        availableIssues: []
      , selectedIssue: null
    }
  }

  render() {
    console.log("App rendering")
    return(
      <div className="previewsApp">
        <div className="controlBar">
          <IssuePickerContainer doneSelectIssue={this.handleIssueSelected.bind(this)} availableIssues={this.state.availableIssues}/>
          <OrderDetails />
        </div>
        <PreviewsGrid selectedIssue={this.state.selectedIssue}/>
      </div>
    )
  }

  handleIssueSelected(selectedIssue) {
    this.setState({
      selectedIssue: selectedIssue
    })
  }

}
