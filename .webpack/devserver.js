const webpack = require('webpack');
const NpmInstallPlugin = require('npm-install-webpack-plugin');

module.exports = function (paths) {
  return {
    devServer: {
      contentBase: paths.build,
      historyApiFallback: true,
      hot: true,
      inline: true,
      progress: true,
      stats: 'errors-only',
      host: process.env.HOST,
      port: process.env.PORT,
      devtool: 'eval-source-map',
    },
    plugins: [
      new webpack.HotModuleReplacementPlugin(),
      new NpmInstallPlugin({
        save: true,
      }),
    ],
  };
};
