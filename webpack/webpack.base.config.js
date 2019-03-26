const path = require("path");


module.exports = {
  mode: "none",
  context: __dirname,

  entry: {
      login: "../frontend/src/react/app",
      semantic: "semantic-ui-css/semantic.min.css",
      add_item: "../frontend/src/react/components/addItem/app",
  },

  devtool: "inline-source-map",

  devServer: {
    headers: {
      "Access-Control-Allow-Origin": "*"
    },
    hot: null
  },

  output: {
    path: path.resolve("./static/bundles/"),
    filename: "[name]-[hash].js"
  },

  plugins: [
  ],

  module: {
    rules: [] // add all common loaders here
  },

  optimization: {
    minimizer: []
  },

  resolve: {
    extensions: [".js", ".jsx", ".scss", ".sass"],
    // alias: {'react-dom': '@hot-loader/react-dom'}
  }
};
