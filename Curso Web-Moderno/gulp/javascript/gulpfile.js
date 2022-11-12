const { series } = require('gulp')
const gulp = require('gulp')
const concat = require('gulp-concat')
const uglify = require('gulp-uglify')
const babel = require('gulp-babel')

function padrao(cb) {
    return gulp.src('./src/**/*.js')
        .pipe(babel({
            comments: false,
            presets: ["enV"]
        }))
        .pipe(uglify())
        .on('error', err => console.log(err))
        .pipe(concat('codigo.min.js'))
        .pipe(gulp.dest('build'))
}

function fim() {
    return console.log('Codigo Finalizado.')
}

exports.default = series(padrao, fim)