const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: {
    app: './graph/src/test.js'
  },
  output: {
    path: path.resolve(__dirname, 'public'),
    filename: './index.js'
  },
  module: {
    loaders: [{
      test: /\.js$/,
      exclude: /node_modules/,
      loader: 'babel-loader',
      query: {
        presets: ['env', 'react']
      }
    },
    {
      test: /\.css$/,
      exclude: /node_modules/,
      loader: ['style-loader', 'css-loader']
    },
    {
      test: /\.png$/,
      exclude: /node_modules/,
      use: [
        'file-loader',
        {
          loader: 'image-webpack-loader',
          options: {
            optipng: { optimizationLevel: 7 },
            pngquant: { quality: "65-90", speed: 4 }
          }
        }]
    }]
  },
  plugins: [new HtmlWebpackPlugin({ template: './graph/src/index.html' })]
};
