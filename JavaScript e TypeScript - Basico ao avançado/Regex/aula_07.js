const { cpfs2 } = require('./base')

// ^ -> Começa com
// $ -> Termina com
// [^] -> Negação
// m -> Multline

const cpfRegExp = /^(\d{3}\.){2}\d{3}\-\d{2}/g
const cpf = "215.978.456-12"
console.log(cpf.match(cpfRegExp))