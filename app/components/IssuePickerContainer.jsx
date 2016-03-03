import React from 'react'
import IssueSelect from './IssueSelect.jsx'
import R from 'ramda'

export default class IssuePickerContainer extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      issues: props.availableIssues
    }
  }

  render() {
    console.log("Rendering the container :", this.state.issues)
    const issues = R.map(R.prop('issue'), this.state.issues)
    return <IssueSelect onSelectIssue={this.handleSelectIssue.bind(this, this.props)} issues={issues} />
  }

  handleSelectIssue(props, selectedIssue) {
    if (props.doneSelectIssue) props.doneSelectIssue(selectedIssue)
  }
}
