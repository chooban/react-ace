import React from 'react';
import { map } from 'ramda';

export default React.createClass({
  displayName: 'IssueSelect',
  propTypes: {
    issues: React.PropTypes.array,
    onSelectIssue: React.PropTypes.func,
  },
  componentDidMount() {
    this.props.onSelectIssue(this.props.issues[0]);
  },

  renderIssue(issueNumber) {
    return <option key={issueNumber}>{issueNumber}</option>;
  },

  handleSelected(props, e) {
    if (props.onSelectIssue) {
      props.onSelectIssue(e.currentTarget.selectedOptions[0].value);
    }
  },

  render() {
    return (
      <div>
        <span>Pick an issue: </span>
        <select onChange={this.handleSelected.bind(this, this.props)}>
          {map(this.renderIssue, this.props.issues)}
        </select>
      </div>
    );
  },
});
