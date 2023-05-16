const { texto } = require("./base");
const regExp = /João|maria/gi;

// console.log(texto.match(regExp))
// console.log(texto.replace(regExp, 'Lucas'))
// console.log(texto.replace(/(João|maria)/gi, '<b>$1</b>'))
console.log(texto.replace(/(João|maria)/gi, function(input) {
    return `<name>${input.toLocaleUpperCase()}</name>`
}))