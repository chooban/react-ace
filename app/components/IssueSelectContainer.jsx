import {createClass} from 'react'
import IssueSelect from './IssueSelect.jsx'
import PreviewsStore from '../stores/PreviewsStore'
import {getIssues} from '../actions/PreviewsActions'
import {changedIssue} from '../actions/PreviewsActions'
import {map,prop} from 'ramda'

const indexByIssue = map(prop('issue'))

export default createClass({
    displayName: 'IssueSelect'
  , getInitialState() {
      return {
        issues: []
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
        issues: indexByIssue(PreviewsStore.getIssues())
      })
  }
  , onSelectIssue(issue) {
      changedIssue(issue)
  }
  , render() {
      return( <IssueSelect issues={this.state.issues} onSelectIssue={this.onSelectIssue}/> )
  }
})
