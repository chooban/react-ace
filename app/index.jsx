import getBootstrapInfo from './utils/BootstrapService';

const run = () => {
  // eslint-disable-next-line
  console.log('Bootstrapping...');
  getBootstrapInfo().then(() => {
    // eslint-disable-next-line
    console.log('Starting app...');
    // eslint-disable-next-line
    const startApp = require('./StartApp').default;
    startApp();
  });
};

if (!Object.assign) {
  require.ensure([], () => {
    require('babel-polyfill'); //eslint-disable-line
    run();
  }, 'polyfill');
} else {
  run();
}

