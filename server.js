const webpack = require("webpack");
const WebpackDevServer = require("webpack-dev-server");
const config = require("./webpack/webpack.local.config");

const hostname = "inventory.developers.localhost";
const port = 8080;

const options = {
  publicPath: config.output.publicPath,
  hot: true,
  inline: true,
  host: "inventory.developers.localhost", // In hosts files create a passage for this endpoint => (localhost   mwebaza.localhost)
  proxy: {
    "**": "http://inventory.developers.localhost:8000",
    "secure": false,
  },
  headers: {
    "Access-Control-Allow-Origin": "*",
  },
  historyApiFallback: true
};

WebpackDevServer.addDevServerEntrypoints(config, options);

const compiler = webpack(config);
const server = new WebpackDevServer(compiler, options);

server.listen(port, hostname, (err, result) => {
  if (err) {
    console.error(err);
  }
});
