const webpack = require('webpack');
const HtmlPlugin = require('html-webpack-plugin');

module.exports = function() {
  return {
    devtool: 'source-map',
    plugins: [
      new HtmlPlugin({
        isProd: 'true',
        filename: 'index.html',
        template: 'public/index.hbs'
      }),
      new webpack.optimize.UglifyJsPlugin({
        sourceMap: true,
        compress: {
          warnings: false,
        },
        comments: false
      }),
      new webpack.DefinePlugin({
        'process.env': {
          NODE_ENV: JSON.stringify('production'),
        },
      }),
    ],
  };
}
