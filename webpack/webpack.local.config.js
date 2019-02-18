const path = require("path");
const webpack = require("webpack");
const BundleTracker = require("webpack-bundle-tracker");
const ExtractTextPlugin = require("extract-text-webpack-plugin");
const config = require("./webpack.base.config.js");

config.mode = "development";
// Use webpack dev server
config.entry = {
  // hotLoader: 'webpack/hot/dev-server',
  login: "../frontend/src/react/app",
  semantic: "semantic-ui-css/semantic.min.css"
};
  // "webpack-dev-server/client?http://0.0.0.0:7070/",
  // "webpack/hot/only-dev-server",
  // "react-hot-loader/patch",
// ];

// override django"s STATIC_URL for webpack bundles
config.output.publicPath = "http://inventory.developers.localhost:7070/static/bundles/";

config.plugins = config.plugins.concat([
  new webpack.HotModuleReplacementPlugin(),
  new BundleTracker({filename: "./webpack-stats.json"}),
  new ExtractTextPlugin({
     filename: "[name].[hash].css",
   }),
]);

// Add a loader for JSX files with react-hot enabled
config.module.rules.push(
  { test: /\.jsx?$/, exclude: /node_modules/, loader: "babel-loader" },
  { test: /\.(scss|css)$/, use: ExtractTextPlugin.extract({
          fallback: "style-loader",
          use: ["css-loader", "sass-loader"]
        })},
  { test: /\.less$/, use: ExtractTextPlugin.extract({
          fallback: "style-loader",
          use: ["css-loader", "less-loader"]
        })},
  { test: /\.jpe?g$|\.gif$|\.ico$|\.png$|\.svg$/, loader: "file-loader?name=[name].[ext]?[hash]" },
  { test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: "url-loader?limit=10000&mimetype=application/font-woff" },
  { test: /\.(ttf|eot)(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: "file-loader?name=" },
  { test: /\.(ttf|eot)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
    use: "file-loader?name=/fonts/[name].  [ext]&mimetype=application/font-otf" },
);

module.exports = config;
