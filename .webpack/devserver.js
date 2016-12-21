const webpack = require('webpack');
const NpmInstallPlugin = require('npm-install-webpack-plugin');

module.exports = function (paths) {
  return {
    devServer: {
      contentBase: paths.build,
      historyApiFallback: true,
      hot: true,
      inline: true,
      stats: 'errors-only',
      host: '0.0.0.0',
      port: 3000,
      proxy: {
        '/api/previews': {
          target: 'http://previewsapi:8100',
          pathRewrite: { '^/api/previews' : '/previews' }
        },
        '/api/orders': {
          target: 'http://ordersapi:8100',
          pathRewrite: { '^/api/orders' : '/orders' }
        }
      }
    },
    plugins: [
      new webpack.HotModuleReplacementPlugin(),
      new NpmInstallPlugin({
        save: true,
      }),
      new webpack.DefinePlugin({
        'process.env': {
          NODE_ENV: JSON.stringify('development'),
        },
      }),
    ],
  };
};
