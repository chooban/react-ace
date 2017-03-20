const webpack = require('webpack');
const HtmlPlugin = require('html-webpack-plugin');
const CopyPlugin = require('copy-webpack-plugin');

const config = function configFactory(paths) {
  return {
    devtool: 'cheap-module-source-map',
    entry: {
      app: [
        paths.app,
        'whatwg-fetch'
      ],
      polyfill: [
        'babel-polyfill'
      ],
      vendor: [
        'auth0-lock',
        'react',
        'react-dom',
        'react-redux',
        'redux',
        'redux-actions',
        'redux-logger',
        'redux-thunk',
        'sprintf'
      ]
    },
    resolve: {
      extensions: ['.js', '.jsx', '.css']
    },
    output: {
      path: paths.build,
      filename: '[name].js'
    },
    module: {
      rules: [
        {
          test: /\.css$/,
          loader: 'style-loader!css-loader',
          include: paths.app
        }, {
          test: /\.jsx?$/,
          loader: 'babel-loader',
          include: paths.app
        },
        {
          test: /\.jsx?$/,
          loader: 'eslint-loader',
          include: paths.app,
          enforce: 'pre',
          options: {
            failOnWarning: false,
            failOnError: false
          }
        }
      ]
    },
    plugins: [
      new HtmlPlugin({
        title: 'Ace My Order',
        template: 'public/index.html'
      }),
      new webpack.ProvidePlugin({
        Promise: 'es6-promise', // Thanks Aaron (https://gist.github.com/Couto/b29676dd1ab8714a818f#gistcomment-1584602),
        fetch: 'imports-loader?this=>global!exports-loader?global.fetch!whatwg-fetch'
      }),
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
