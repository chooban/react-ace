import { connect } from 'react-redux';
import IssueSelect from '../components/IssueSelect';
import { map, prop } from 'ramda';
import { requestIssue } from '../actions';

const indexByIssue = map(prop('issue'));

const mapStateToProps = (state) => {
  return {
    issues: state.issues.issuesList
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    onSelectIssue: (issueNumber) => {
      dispatch(requestIssue(issueNumber));
    }
  }
}

const IssueSelectContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(IssueSelect);

export default IssueSelectContainer;
