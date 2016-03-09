import React from 'react'
import IssueSelect from './IssueSelect.jsx'
import PreviewsStore from '../stores/PreviewsStore'
import {getIssues} from '../actions/PreviewsActions'
import {choseIssue} from '../actions/ChosenIssueActions'
import R from 'ramda'

const indexByIssue = R.map(R.prop('issue'))

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
      getIssues()
  }
  , componentWillUnmount() {
      PreviewsStore.removeChangeListener(this.onStoreChange)
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
      const issues = indexByIssue(this.state.all)
      return( <IssueSelect issues={issues} onSelectIssue={this.onSelectIssue}/> )
  }
})
