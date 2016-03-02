import React from 'react'
import IssueSelect from './IssueSelect.jsx'

export default class IssuePickerContainer extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      issues: []
    }
  }

  componentDidMount() {
    this.setState({
      issues: [
        100
      , 101
      , 102
      ]
    })
  }

  render() {
    return <IssueSelect onSelectIssue={this.handleSelectIssue} issues={this.state.issues} />
  }

  handleSelectIssue(selectedIssue) {
    console.log(selectedIssue)
  }
}
