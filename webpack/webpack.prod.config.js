const webpack = require("webpack");
const BundleTracker = require("webpack-bundle-tracker");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const config = require("./webpack.base.config.js");
const UglifyJsPlugin = require("uglifyjs-webpack-plugin");
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");

config.mode = "production";

config.output.path = require("path").resolve("staticfiles/bundles");

config.entry = {
  // hotLoader: 'webpack/hot/dev-server',
  login: "../frontend/src/react/app",
  semantic: "semantic-ui-css/semantic.min.css"
};

config.plugins = config.plugins.concat([
  new BundleTracker({filename: "./webpack-stats-prod.json"}),
  new MiniCssExtractPlugin({
    // Options similar to the same options in webpackOptions.output
    // both options are optional
    filename: "[name][hash].css",
    chunkFilename: "[id].css"
  }),
  // removes a lot of debugging code in React
  new webpack.DefinePlugin({
    "process.env": {
      "NODE_ENV": JSON.stringify("production")
    }}),

]);

config.output.publicPath = "https://i-development.herokuapp.com/static/bundles/";

config.optimization.minimizer.push(
  new UglifyJsPlugin({
    cache: true,
    parallel: true,
    sourceMap: false
  }),
  new OptimizeCSSAssetsPlugin({})
)

// Add a loader for JSX files
config.module.rules.push(
  { test: /\.jsx?$/, exclude: /node_modules/, loader: "babel-loader" },
  {
        test: /\.css$/,
        use: [
          MiniCssExtractPlugin.loader,
          "css-loader"
        ]
    },
  {
    test: /\.scss$/,
    exclude: /node_modules/,
    use: [
      MiniCssExtractPlugin.loader,
      "css-loader",
      "resolve-url-loader",
      "sass-loader",
    ]
  },
  { test: /\.jpe?g$|\.gif$|\.ico$|\.png$|\.svg$/, use: "file-loader?name=[name].[ext]?[hash]" },
  { test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: "url-loader?limit=30000&mimetype=application/font-woff" },
  { test: /\.(ttf|eot)(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: "file-loader?name=" },
  { test: /\.(ttf|eot)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
    use: "file-loader?name=/fonts/[name].  [ext]&mimetype=application/font-otf" },
);

module.exports = config;
