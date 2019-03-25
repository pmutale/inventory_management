const webpack = require("webpack");
const WebpackDevServer = require("webpack-dev-server");
const config = require("./webpack/webpack.local.config");

const hostname = "inventory.developers.localhost";
const port = 7070;

new WebpackDevServer(webpack(config), {
  publicPath: config.output.publicPath,
  hot: true,
  inline: true,
  host: "inventory.developers.localhost", // In hosts files create a passage for this endpoint => (localhost   mwebaza.localhost)
  proxy: {
    "**": "http://inventory.developers.localhost:7000",
    "secure": false,
  },
  headers: {
      "Access-Control-Allow-Origin": "*",
    },
  historyApiFallback: true
}).listen(port, hostname, function (err, result) {
  if (err) {
    console.error(err);
  }

  console.log("Listening at 0.0.0.0:7070");
  console.log("Entry", config.entry);
});
