const path = require('path');
const webpack = require('webpack');
const merge = require('webpack-merge');
const devConfig = require('./conf/devServer');

const TARGET = process.env.npm_lifecycle_event;
process.env.BABEL_ENV = TARGET;

const PATHS = {
  app: path.join(__dirname, 'app'), build: path.join(__dirname, 'build'),
};

const common = {
  devtool: 'cheap-module-source-map',
  entry: {
    app: PATHS.app,
  },
  resolve: {
    extensions: ['', '.js', '.jsx'],
  },
  output: {
    path: PATHS.build,
    filename: 'bundle.js',
  },
  node: {
    fs: 'empty',
  },
  module: {
    loaders: [
      {
        test: /\.css$/,
        loader: 'style-loader!css-loader',
        include: PATHS.app,
      }, {
        test: /\.jsx?$/,
        loader: 'babel',
        include: PATHS.app,
      },
    ],
  },
  plugins: [
    new webpack.optimize.DedupePlugin(),
    new webpack.ContextReplacementPlugin(/moment[\\\/]locale$/, /^\.\/(en-gb|uk)$/),
    new webpack.ProvidePlugin({
      Promise: 'imports?this=>global!exports?global.Promise!es6-promise',
      fetch: 'imports?this=>global!exports?global.fetch!whatwg-fetch',
    }),
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: JSON.stringify('production'),
      },
    })
  ],
};

if (TARGET === 'start' || !TARGET) {
  // module.exports = merge(common, devConfig(PATHS.build))
  module.exports = merge(common, {});
}

if (TARGET === 'build') {
  common.plugins.push(new webpack.optimize.UglifyJsPlugin({
      compress:{
        warnings: false,
      },
  })):
  module.exports = merge(common, {});
}
