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
        'material-ui',
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
        },
        {
          test: /\.hbs$/,
          loader: 'handlebars-loader'
        }
      ]
    },
    plugins: [
      new HtmlPlugin({
        filename: 'index.html',
        template: 'public/index.hbs'
      }),
      new HtmlPlugin({
        filename: 'privacy.html',
        template: 'public/privacy.hbs',
        chunks: []
      }),
      new HtmlPlugin({
        filename: 'contact.html',
        template: 'public/contact.hbs',
        chunks: []
      }),
      new HtmlPlugin({
        filename: 'about.html',
        template: 'public/about.hbs',
        chunks: []
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
