import React from 'react';

export default React.createClass({
  displayName: 'IssueSelect',

  propTypes: {
    issues: React.PropTypes.array,
    onSelectIssue: React.PropTypes.func,
  },

  renderIssue(issueNumber) {
    return <option key={issueNumber}>{issueNumber}</option>;
  },

  handleSelected(e) {
    if (this.props.onSelectIssue) {
      const target = e.currentTarget.selectedOptions[0];
      this.props.onSelectIssue(target.value);
    }
  },

  render() {
    return (
      <div>
        <span>Pick an issue: </span>
        <select
          onChange={this.handleSelected}
          >
          {this.props.issues.map(function(issue, idx) {
            return (<option key={issue} value={issue}>{issue}</option>);
          })}
        </select>
      </div>
    );
  },
});
