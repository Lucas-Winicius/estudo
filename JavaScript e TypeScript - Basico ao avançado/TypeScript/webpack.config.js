// eslint-disable-next-line @typescript-eslint/no-var-requires
const path = require("path");

module.exports = {
  mode: "development",
  entry: "./source/A018-webpack/index.ts",
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: "ts-loader",
        exclude: /node_modules/,
      },
    ],
  },
  resolve: {
    extensions: [".tsx", ".ts", ".js"],
  },
  output: {
    filename: "bundle.js",
    path: path.resolve(__dirname, "dist"),
  },
  devtool: "source-map",
};
