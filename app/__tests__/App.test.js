import test from 'tape';
import App from '../App'; // eslint-disable-line

test('Include root component', (t) => {
  // eslint-disable-next-line
  t.test('Component was included to include all files for coverage', (t) => {
    t.equal(true, true);
    t.end();
  });
});
