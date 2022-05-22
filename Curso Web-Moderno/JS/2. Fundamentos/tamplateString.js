const nome = 'Lucas'
const concatenacao = 'Olá' + nome + '!'
const tamplate = `
    Olá
    ${nome}!`
console.log(tamplate, concatenacao)

// EXPRESSOES
console.log(`1 + 1 = ${1 + 1}`)

const up = texto => texto.toUpperCase()

console.log(`OLÁ ${up(nome)}`)