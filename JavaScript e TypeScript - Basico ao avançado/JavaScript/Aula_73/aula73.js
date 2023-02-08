const produto = {
  nome: 'Caneta Azul',
  preco: 1.8,
};

// Duplicando o array
const produtoCopia = { ...produto, emEstoque: false };
const produtoCopia2 = Object.assign({}, produto, { emEstoque: true });
const produtoCopia3 = { nome: produto.nome, preco: produto.preco };

// Exibindo somente as keys ( chaves )
const chaves = Object.keys(produto)

// Congelando o objeto
Object.freeze(produto)

// Exibindo propriedades do objeto
const propriedades = Object.getOwnPropertyDescriptor(produto, 'nome')

// Exibindo somente os valores
const valores = Object.values(produto)

// Exibindo chaves e valores
const chavesValores = Object.entries(produto)
// output: [ [ 'nome', 'Caneta Azul' ], [ 'preco', 1.8 ] ]