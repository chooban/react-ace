const webpack = require('webpack');
const HtmlPlugin = require('html-webpack-plugin');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin')

module.exports = function() {
  return {
    devtool: 'source-map',
    plugins: [
      new HtmlPlugin({
        isProd: 'true',
        filename: 'index.html',
        template: 'public/index.hbs'
      }),
      new UglifyJsPlugin({
        sourceMap: true,
        cache: true,
        uglifyOptions: {
          compress: {
            warnings: true
          },
          comments: false
        }
      }),
      new webpack.DefinePlugin({
        'process.env': {
          NODE_ENV: JSON.stringify('production'),
        },
      }),
    ],
  };
}
