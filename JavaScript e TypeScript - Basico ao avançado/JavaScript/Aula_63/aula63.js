const nomes = ['Maria', 'João', 'Eduardo', 'Gabriel', 'Júlia']

// nomes.splice(inicioIndice, qtdADeletar, adicionar1, adicionar2, adicionar3, adicionar4, adicionar5, ...)

// pop
nomes.splice(4, 1)
nomes.splice(-1, 1)

// shift
nomes.splice(0, 1)

// push
nomes.splice(nomes.length, 0, 'Clara')

// unshift
nomes.splice(0, 0, 'Junior')

// Remove da parte selecionada ate o final
/*  nomes.splice(-2, Number.MAX_VALUE)  */

const removidos = nomes.splice(3, 1, 'Gabriel', 'Júlia')

console.log(nomes)