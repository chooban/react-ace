const webpack = require('webpack');
const HtmlPlugin = require('html-webpack-plugin');

const config = function(paths) {
  return {
    devtool: 'cheap-module-source-map',
    entry: {
      app: paths.app,
      vendor: [
        'react',
        'react-dom',
        'react-redux',
        'redux-thunk',
        'redux-logger'
      ]
    },
    resolve: {
      extensions: ['', '.js', '.jsx', '.css'],
    },
    output: {
      path: paths.build,
      filename: 'bundle.js',
    },
    node: {
      fs: 'empty',
    },
    module: {
      preLoaders: [
        {
          test: /\.jsx?$/,
          loader: 'eslint',
          include: paths.app
        }
      ],
      loaders: [
        {
          test: /\.css$/,
          loader: 'style!css',
          include: paths.app,
        }, {
          test: /\.jsx?$/,
          loader: 'babel',
          include: paths.app,
        },
      ],
    },
    eslint: {
      failOnWarning: false,
      failOnError: false
    },
    devtool: 'eval-source-map',
    plugins: [
      new webpack.optimize.DedupePlugin(),
      new HtmlPlugin({
        title: "Ace My Order",
        template: "public/index.html"
      }),
      new webpack.ContextReplacementPlugin(/moment[\\\/]locale$/, /^\.\/(en-gb|uk)$/),
      new webpack.ProvidePlugin({
        Promise: 'imports?this=>global!exports?global.Promise!es6-promise',
        fetch: 'imports?this=>global!exports?global.fetch!whatwg-fetch',
      }),
      new webpack.optimize.CommonsChunkPlugin('vendor', 'vendor.js', Infinity)
    ],
  };
}

module.exports = config;
