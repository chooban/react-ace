import React from 'react'
import Ramda from 'ramda'

export default class IssueSelect extends React.Component {
  constructor(props) {
    super(props)
  }

  render() {
    var issues = Ramda.map(this.renderIssue, this.props.issues)
    return(
      <div>
        <span>Pick an issue: </span>
        <select onChange={this.handleSelected.bind(this, this.props)}>
          {issues}
        </select>
      </div>
    )
  }

  renderIssue(issueNumber) {
    return <option key={issueNumber}>{issueNumber}</option>
  }

  handleSelected(props, e) {
    if (props.onSelectIssue) {
      props.onSelectIssue(e.currentTarget.selectedOptions[0].value)
    } else {
      console.log("No handler")
    }
  }
}
