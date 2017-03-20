const webpack = require('webpack');
const DashboardPlugin = require('webpack-dashboard/plugin');

module.exports = function devconfig(paths) {
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
          pathRewrite: { '^/api/previews': '/previews' }
        },
        '/api/orders': {
          target: 'http://ordersapi:8101',
          pathRewrite: { '^/api/orders': '/orders' }
        },
        '/api/profiles': {
          target: 'http://profilesapi:8101',
          pathRewrite: { '^/api/profiles': '/profiles' }
        }
      }
    },
    plugins: [
      new webpack.HotModuleReplacementPlugin(),
      new webpack.DefinePlugin({
        'process.env': {
          NODE_ENV: JSON.stringify('development')
        }
      }),
      new DashboardPlugin()
    ]
  };
};
