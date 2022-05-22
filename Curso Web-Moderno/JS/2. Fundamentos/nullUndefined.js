/**
 * undefined ->> Variavel foi declarada mas não foi inicializada
 * null ->> Uma variavel "vazia" e que nao aponta para nenhum endereço
*/


let valor // NÃO INICIALIZADA

console.log(valor)
/* console.log(valor2) //NÃO DECLARADO */

valor = null // AUSENCIA DE VALOR
console.log(valor)

const produto = {}

console.log(produto.preco)
console.log(produto)

produto.preco = 3.53
console.log(produto.preco)
