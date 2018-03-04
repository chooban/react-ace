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
        '/api/*': {
          target: 'http://ace:8100',
          pathRewrite: { '^\/api': '' }
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
