const path = require("path");


module.exports = {
  mode: "",
  context: __dirname,

  // entry: [],

  devtool: "inline-source-map",

  devServer: {
    headers: {
      "Access-Control-Allow-Origin": "*"
    }
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
}
