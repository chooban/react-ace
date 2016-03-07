import React from 'react'
import ChosenIssueStore from '../stores/ChosenIssueStore'
import PreviewsStore from '../stores/PreviewsStore'
import PreviewsGrid from './PreviewsGrid'
import {getIssue} from '../actions/PreviewsActions'
import {GET_ISSUE} from '../consts'

export default React.createClass({
    displayName: "PreviewsGridContainer"
  , propTypes : {
      selectedIssue: React.PropTypes.number
    }
  , getInitialState() {
      return {
        chosenIssue: null
      , issueData: null
      }
  }
  , componentWillMount() {
      ChosenIssueStore.addChangeListener(this.setChosenIssue)
  }
  , setChosenIssue() {
      this.setState({
        chosenIssue: ChosenIssueStore.getChosenIssue()
      })
  }
  , render() {
      const msg = (this.state.chosenIssue)
                    ? "Selected issue is " + this.state.chosenIssue
                    : "No issue currently selected"

      console.log(msg)

      return(
        <div className="previewsGridContainer">
          <p>{msg}</p>
          <PreviewsGrid issueNumber={this.state.chosenIssue}/>
        </div>
      )
  }
})
