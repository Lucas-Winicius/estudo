const { alfabeto } = require('./base')

// [abc] -> Conjunto
// [^]   -> Negação
// [-]   -> de x a y sempre em ordem crescente

const regExp1 = /[abc123]/g
const regExp2 = /[abc]+/g
const regExp3 = /[abc123]+/g
const regExp4 = /[^abc123]/g
const regExp5 = /[^abc123]+/g
const regExp6 = /[0-9]/g
const regExp7 = /[a-zA-Z-0-9]/g
const regExp8 = /[a-zA-Z-0-9]+/g
const regExp9 = /[^a-zA-Z-0-9]+/g
const regExp10 = /[\u00A0-\u00BA]+/g

console.log(alfabeto.match(regExp10))