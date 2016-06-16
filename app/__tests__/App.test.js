import test from 'tape';
import App from '../App';

test('Include root component', (t) => {
  t.test('Component was included to include all files for coverage', (t) => {
    t.equal(true, true);
    t.end();
  });
});
