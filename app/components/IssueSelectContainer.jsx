import React from 'react';
import IssueSelect from './IssueSelect.jsx';
import PreviewsStore from '../stores/PreviewsStore';
import { changedIssue } from '../actions/PreviewsActions';
import { map, prop } from 'ramda';

const indexByIssue = map(prop('issue'));

export default React.createClass({
  displayName: 'IssueSelect',
  getInitialState() {
    return {
      issues: [],
      selected: null
    };
  },

  componentWillMount() {
    PreviewsStore.addChangeListener(this.onPreviewsStoreChange);
  },

  componentWillUnmount() {
    PreviewsStore.removeChangeListener(this.onPreviewsStoreChange);
  },

  onPreviewsStoreChange() {
    this.setState({
      issues: PreviewsStore.getIssues()
    });
  },

  render() {
    return (<IssueSelect
              issues={this.state.issues}
              onSelectIssue={changedIssue}
            />);
  },
});
