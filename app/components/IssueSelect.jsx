import React from 'react'
import Ramda from 'ramda'

export default React.createClass({
    displayName: "IssueSelect"
  , propTypes: {
        issues: React.PropTypes.array
      , onSelectIssue: React.PropTypes.func
    }
  , componentDidMount() {
      // First render only, I hope
      this.props.onSelectIssue(this.props.issues[0])
    }
  , render() {
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
  , renderIssue(issueNumber) {
      return <option key={issueNumber}>{issueNumber}</option>
    }
  , handleSelected(props, e) {
      if (props.onSelectIssue) {
        props.onSelectIssue(e.currentTarget.selectedOptions[0].value)
      } else {
        console.log("No handler")
      }
    }
})
