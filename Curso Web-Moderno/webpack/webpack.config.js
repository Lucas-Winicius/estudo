const modoDev = process.env.NODE_ENV !== 'production'
const webpack = require('webpack')
const miniCssExtractPlugin = require('mini-css-extract-plugin')
const uglifyJSPlugin = require('uglifyjs-webpack-plugin')
const optimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin')


module.exports = {
    mode: modoDev ? 'development' : 'production',
    entry: './src/principal.js',
    output: {
        filename: 'principal.js',
        path: __dirname + '/dist'
    },
    plugins: [
        new miniCssExtractPlugin({
            filename: 'estilo.css'
        })
    ],
    devServer: {
        static: './dist',
        port: 9000,
        compress: true
    },
    optimization: {
        minimizer: [ 
            new uglifyJSPlugin({ cache: true, parallel: true }),
            new optimizeCSSAssetsPlugin({})
         ]
    },
    module: {
        rules: [
            { test: /\.s?[ac]ss$/, use: [ miniCssExtractPlugin.loader, 'css-loader', 'sass-loader' ] },
            { test: /\.(png|svg|jpg|jpeg|gif)$/, use: [ 'file-loader' ] }
        ]
    }
}