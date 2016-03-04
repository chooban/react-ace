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
    entry: {
      app: PATHS.app
    }
  , resolve: {
      extensions: ['', '.js', '.jsx']
  }
  , output: {
      path: PATHS.build
    , filename: 'bundle.js'
  }
  , module: {
    loaders: [
      {
        test: /\.css$/
      , loaders: ['style', 'css']
      , include: PATHS.app
      }
    , {
        test: /\.jsx?$/
        // Enable caching for improved performance during development
        // It uses default OS directory by default. If you need something
        // more custom, pass a path to it. I.e., babel?cacheDirectory=<path>
      , loaders: ['babel?cacheDirectory']
        // Parse only app files! Without this it will go through entire project.
        // In addition to being slow, that will most likely result in an error.
      , include: PATHS.app
      }
    ]
  }
}

if (TARGET === 'start' || !TARGET) {
  module.exports = merge(common, devConfig(PATHS.build))
  // module.exports = merge(common, {})
}

if (TARGET === 'build') {
  module.exports = merge(common, {})
}
