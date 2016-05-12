const path = require('path')
const webpack = require('webpack')
const merge = require('webpack-merge')
const devConfig = require('./conf/devServer')

const TARGET = process.env.npm_lifecycle_event
process.env.BABEL_ENV = TARGET;

const PATHS = {
  app: path.join(__dirname, 'app')
, build: path.join(__dirname, 'build')
}

const common = {
    devtool: 'cheap-module-source-map'
  , entry: {
      app: PATHS.app
    }
  , resolve: {
      extensions: ['', '.js', '.jsx']
  }
  , output: {
      path: PATHS.build
    , filename: 'bundle.js'
  }
  , node: {
      fs: "empty"
  }
  , module: {
      loaders: [
        {
          test: /\.css$/
        , loader: 'style-loader!css-loader'
        , include: PATHS.app
        }
      , {
          test: /\.jsx?$/
        , exclude: /(node_modules|__tests__)/
        , loader: 'babel-loader'
        , query: {
            presets: ['react', 'es2015']
        }
        , include: PATHS.app
        }
      ]
  }
  , plugins: [
      new webpack.optimize.DedupePlugin()
    , new webpack.ContextReplacementPlugin(/moment[\\\/]locale$/, /^\.\/(en-gb|uk)$/)
    , new webpack.ProvidePlugin({
          Promise: 'imports?this=>global!exports?global.Promise!es6-promise'
        , fetch: 'imports?this=>global!exports?global.fetch!whatwg-fetch'
      })
    , new webpack.DefinePlugin({
        'process.env': {
          'NODE_ENV': '"production"'
        }
      })
    // , new webpack.optimize.UglifyJsPlugin({
    //     compress: {
    //       warnings: false
    //     }
    //   })
  ]
}

if (TARGET === 'start' || !TARGET) {
  // module.exports = merge(common, devConfig(PATHS.build))
  module.exports = merge(common, {})
}

if (TARGET === 'build') {
  module.exports = merge(common, {})
}
