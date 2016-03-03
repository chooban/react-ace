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

  componentDidMount() {
    /*
    d3.json('http://nginx-previews-861f5682-1.chooban.cont.tutum.io/previews', function(error, listOfIssues) {
      this.setState({
        availableIssues: listOfIssues
      })
    }.bind(this))
    */
    console.log("App mounted")
    this.setState({
      availableIssues: [{"issue": 324}]
    }, function() {
      console.log("Rerendered")
      console.log(JSON.stringify(this.state))
    })
  }

  handleIssueSelected(selectedIssue) {
    this.setState({
      selectedIssue: selectedIssue
    })
  }

}
