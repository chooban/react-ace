/* eslint no-shadow: 0 */
import test from 'tape';
import App from '../App'; //eslint-disable-line

test('Include root component', (t) => {
  t.test('Component included for file coverage reasons', (t) => {
    t.equal(true, true);
    t.end();
  });
});
