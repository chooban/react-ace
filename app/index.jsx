import getBootstrapInfo from './utils/BootstrapService';
import startApp from './StartApp';

const run = () => {
  // eslint-disable-next-line
  console.log('Bootstrapping...');
  getBootstrapInfo().then(() => {
    // eslint-disable-next-line
    console.log('Starting app...');
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

