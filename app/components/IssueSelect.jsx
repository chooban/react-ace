import React from 'react'

export default class IssueSelect extends React.Component {
  constructor(props) {
    super(props)
  }

  render() {
    return(
      <select>
        {this.props.issues.forEach(this.renderIssue)}
      </select>
    )
  }

  renderIssue(issueNumber) {
    return <option>{issueNumber}</option>
  }

}
