import React from 'react'
import ChosenIssueStore from '../stores/ChosenIssueStore'

export default React.createClass({
    displayName: "PreviewsGrid"
  , propTypes : {
      selectedIssue: React.PropTypes.number
    }
  , getInitialState() {
      return {
          chosenIssue: null
      }
  }
  , componentWillMount() {
      ChosenIssueStore.addChangeListener(this.onChosenIssue)
  }
  , onChosenIssue(issue) {
      this.setState({
        chosenIssue: ChosenIssueStore.getChosenIssue()
      })
      console.log("Set state")
  }
  , render() {
    const msg = (this.state.chosenIssue)
                  ? "Selected issue is " + this.state.chosenIssue
                  : "No issue currently selected"

    return(<div>{msg}</div>)
  }
})
