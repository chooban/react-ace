import { connect } from 'react-redux';
import IssueSelect from '../components/IssueSelect';
import { requestIssue } from '../actions';

const mapStateToProps = (state) => (
  {
    issues: state.issues.issuesList
  }
);

const mapDispatchToProps = (dispatch) => {
  const onSelectIssue = (issueNumber) => dispatch(requestIssue(issueNumber));
  return { onSelectIssue };
};

const IssueSelectContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(IssueSelect);

export default IssueSelectContainer;
