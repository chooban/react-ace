import React from 'react'
import ChosenIssueStore from '../stores/ChosenIssueStore'

export default React.createClass({
    displayName: "PreviewsGrid"
  , propTypes : {
      selectedIssue: React.PropTypes.number
    }
  , componentWillMount() {
      ChosenIssueStore.addChangeListener(this.onChosenIssue)
  }
  , onChosenIssue(issue) {
      console.log("PreviewsGrid: ", ChosenIssueStore.getChosenIssue())
  }
  , render() {
    const msg = (this.props.selectedIssue)
                  ? "Selected issue is " + this.props.selectedIssue
                  : "No issue currently selected"

    return(<div>{msg}</div>)
  }
})
