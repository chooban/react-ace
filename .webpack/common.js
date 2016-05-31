const webpack = require('webpack');

const config = function(paths) {
  return {
    devtool: 'cheap-module-source-map',
    entry: {
      app: paths.app,
      vendor: ['react',
        'react-dom',
        'react-redux',
        'redux-thunk',
        'redux-logger',
        'reactabular',
        'react-pagify',
        'segmentize',
        'ramda'
      ]
    },
    resolve: {
      extensions: ['', '.js', '.jsx'],
    },
    output: {
      path: paths.build,
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
          include: paths.app,
        }, {
          test: /\.jsx?$/,
          loader: 'babel',
          include: paths.app,
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
      new webpack.optimize.CommonsChunkPlugin('vendor', 'vendor.js', Infinity)
    ],
  };
}

module.exports = config;
