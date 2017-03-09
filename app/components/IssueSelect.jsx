import React from 'react';

const devNull = () => {};

const IssueSelect = ({ issues, onSelectIssue = devNull }) => (
  <div>
    <span>Pick an issue: </span>
    <select
      onChange={(e) => {
        const target = e.currentTarget.selectedOptions[0];
        onSelectIssue(target.value);
      }}
    >
      {
      issues.map((issue) => <option key={issue} value={issue}>{issue}</option>)
      }
    </select>
  </div>
);

IssueSelect.propTypes = {
  issues: React.PropTypes.array,
  onSelectIssue: React.PropTypes.func.isRequired
};

IssueSelect.defaultProps = {
  issues: []
};

IssueSelect.displayName = 'Issue Dropdown';

export default IssueSelect;
