/* eslint no-shadow: 0 */
import React from 'react';
import IssueSelect from '../IssueSelect.jsx';
import test from 'tape';
import Ramda from 'ramda';
import { shallow } from 'enzyme';
import sinon from 'sinon';

function shallowRenderIssueSelect(issues, onChangeHandler) {
  return shallow(
    <IssueSelect
      issues={issues}
      onSelectIssue={onChangeHandler}
    />
  );
}

test('Issue Select component', (t) => {
  const issues = [
    '100', '101', '102',
  ];

  t.test('It renders a label and options', (t) => {
    const result = shallowRenderIssueSelect(issues);
    const isOption = Ramda.whereEq({ type: 'option' });
    const options = Ramda.filter(isOption, result.node.props.children[1].props.children);
    t.equal(options.length, 3);
    t.equal(result.node.props.children[0].props.children, 'Pick an issue: ');

    let opt = undefined;
    issues.forEach((issue, idx) => {
      opt = result.node.props.children[1].props.children[idx];
      t.equal(opt.key, issues[idx]);
      t.equal(opt.props.children, issues[idx]);
    });

    t.end();
  });

  t.test('It invokes the passed function on change', (t) => {
    function selectedIssueEvent(issueNumber) {
      return {
        currentTarget: {
          selectedOptions: [`${issueNumber}`],
        },
      };
    }

    const onChangeHandler = sinon.spy();
    const wrapper = shallowRenderIssueSelect(issues, onChangeHandler);
    wrapper.find('select').simulate('change', selectedIssueEvent(101));

    t.equal(onChangeHandler.calledOnce, true);
    t.end();
  });
});

