const array = ['Lucas', 'Leo', 'Maria']

array.pop() // Remove o ultimo
array.shift() // Remove o primeiro
// Ambos retornam o valor removido

array.push('Pedro') // Adiciona no ultimo indice
array.unshift('Brenda') // Adiciona no primeiro indice

const array2 = ['Lucas', 'Leo', 'Maria', 'Pedro', 'Brenda', 'Marcos', 'Luiz']
const novo = array2.slice(0, 4) // Fatia do o array desejado
console.log(novo) // [ 'Lucas', 'Leo', 'Maria', 'Pedro' ]

const novo2 = array2.slice(0, -1)
console.log(novo2) // [ 'Lucas', 'Leo', 'Maria', 'Pedro', 'Brenda', 'Marcos' ]

/**
 * slice NÃO modifica o array original
 * splice MODIFICA o array original
 * apos a modificação o array original ficara com o resto
 * 
 * 
 * ambos retornam o array modificado
 */