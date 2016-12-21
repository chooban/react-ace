const path = require('path');
const merge = require('webpack-merge');
const validate = require('webpack-validator');

const common = require('./.webpack/common');
const productionConfig = require('./.webpack/production');
const devConfig = require('./.webpack/devserver');

const paths = {
  app: path.join(__dirname, 'app/'),
  build: path.join(__dirname, 'build/')
};

const TARGET = process.env.npm_lifecycle_event;
process.env.BABEL_ENV = TARGET;

module.exports = (TARGET === 'build')
  ? validate(merge(common(paths), productionConfig(paths)))
  : validate(merge(common(paths), devConfig(paths)));
