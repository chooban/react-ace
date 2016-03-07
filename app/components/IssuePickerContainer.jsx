import React from 'react'
import IssueSelect from './IssueSelect.jsx'
import PreviewsStore from '../stores/PreviewsStore'
import {getData} from '../actions/PreviewsActions'
import {choseIssue} from '../actions/ChosenIssueActions'
import R from 'ramda'

export default React.createClass({
    displayName: 'IssueSelect'
  , propTypes: {
      all: React.PropTypes.array
    }
  , getInitialState() {
      return {
        all: []
      }
  }
  , componentWillMount() {
      PreviewsStore.addChangeListener(this.onStoreChange)
      getData()
  }
  , onStoreChange() {
      this.setState({
        all: PreviewsStore.getIssues()
      })
  }
  , onSelectIssue(issue) {
      choseIssue(issue)
  }
  , render() {
      const issues = R.map(R.prop('issue'), this.state.all)
      return(
        <div>
          <IssueSelect issues={issues} onSelectIssue={this.onSelectIssue}/>
        </div>
      )
  }
})
