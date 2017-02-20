const webpack = require('webpack');
const HtmlPlugin = require('html-webpack-plugin');
const CopyPlugin = require('copy-webpack-plugin');

const config = function (paths) {
  return {
    devtool: 'cheap-module-source-map',
    entry: {
      app: paths.app,
      polyfill: [
        'babel-polyfill'
      ],
      vendor: [
        'react',
        'react-dom',
        'react-redux',
        'redux',
        'redux-actions',
        'redux-logger',
        'redux-thunk',
        'sprintf'
      ],
      auth: [
        'auth0-lock'
      ]
    },
    resolve: {
      extensions: ['', '.js', '.jsx', '.css']
    },
    output: {
      path: paths.build,
      chunkFilename: '[name].js',
      filename: '[name].js'
    },
    node: {
      fs: 'empty'
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
          include: paths.app
        }, {
          test: /\.jsx?$/,
          loader: 'babel',
          include: paths.app
        }
      ]
    },
    eslint: {
      failOnWarning: false,
      failOnError: false
    },
    plugins: [
      new webpack.optimize.DedupePlugin(),
      new HtmlPlugin({
        title: 'Ace My Order',
        template: 'public/index.html'
      }),
      new webpack.ProvidePlugin({
        Promise: 'es6-promise', // Thanks Aaron (https://gist.github.com/Couto/b29676dd1ab8714a818f#gistcomment-1584602)
        fetch: 'imports?this=>global!exports?global.fetch!whatwg-fetch'
      }),
      new webpack.ContextReplacementPlugin(/moment[\\\/]locale$/, /^\.\/(en-gb|uk)$/),
      new webpack.optimize.CommonsChunkPlugin({
        name: 'vendor'
      }),
      new CopyPlugin([
        { from: 'assets' }
      ])
    ]
  };
};

module.exports = config;
