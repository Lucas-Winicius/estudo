// Operador ... rest(juntar)/spread(espalhar)

// Rest com objeto
const funcionario = { nome: 'Lucas', salario: 12348.99 }
const clone = { ativo: true, ...funcionario }
console.log(clone)

// Spread em array
const grupoA = ['Lucas', 'Maria', 'Leonardo']
const grupoFinal = ['Abobora', ...grupoA]
console.log(grupoFinal)