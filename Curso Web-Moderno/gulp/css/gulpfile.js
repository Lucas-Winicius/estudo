const { series } = require('gulp')
const gulp = require('gulp')
const sass = require('node-sass')(require('sass'));
const uglifyCSS = require('gulp-uglifycss')
const concat = require('gulp-concat')

function transformacaoSASS() {
    return gulp.src('./src/sass/index.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(uglifyCSS({
            "uglyComments": true
        }))
        .pipe(concat('estilo.min.css'))
        .pipe(gulp.dest('build/css'))
}

exports.default = series(transformacaoSASS)