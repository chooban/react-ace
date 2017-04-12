import 'babel-polyfill';
import getBootstrapInfo from './utils/BootstrapService';

const run = () => {
  getBootstrapInfo().then(() => {
    // eslint-disable-next-line
    const startApp = require('./StartApp').default;
    startApp();
  });
};

run();
