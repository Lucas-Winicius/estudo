const { series, parallel } = require('gulp')
const gulp = require('gulp')
const sass = require('gulp-sass')(require('sass'))
const uglifyCSS = require('gulp-uglifycss')
const concat = require('gulp-concat')

function transformacaoSASS() {
    return gulp.src('./src/sass/index.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(uglifyCSS({
            "uglyComments": true
        })) /* ESPAÇOS */
        .pipe(concat('estilo.min.css'))
        .pipe(gulp.dest('build/css'))
}

function tranferirHTML() {
    return gulp.src('./src/index.html')
    .pipe(uglifyCSS({
        "uglyComments": true
    }))
    .pipe(gulp.dest('./build'))
}

exports.default = parallel(transformacaoSASS, tranferirHTML)