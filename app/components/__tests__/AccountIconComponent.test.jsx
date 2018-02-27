/* eslint no-shadow: 0 */
import React from 'react';
import test from 'tape';
import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-15';

import AccountIconComponent from '../AccountIconComponent';
import ProfileIconContainer from '../../containers/ProfileIcon';
import LoginIconContainer from '../../containers/LoginIcon';

configure({ adapter: new Adapter() });

function render(isLoggedIn) {
  return shallow(<AccountIconComponent isLoggedIn={isLoggedIn} />);
}

test('Account Icon choice', (t) => {
  t.test('Is logged in', (t) => {
    const result = render(true);
    t.equal(result.find(ProfileIconContainer).length, 1);
    t.equal(result.find(LoginIconContainer).length, 0);
    t.end();
  });

  t.test('Is not logged in', (t) => {
    const result = render(false);
    t.equal(result.find(ProfileIconContainer).length, 0);
    t.equal(result.find(LoginIconContainer).length, 1);
    t.end();
  });
});
