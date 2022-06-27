const produtos = [
    {nome: 'Notebook', preco: 2499, fragil: true},
    {nome: 'iPad Pro', preco: 4199, fragil: true},
    {nome: 'Copo De Vidro', preco: 12.49, fragil: true},
    {nome: 'Copo De Plastico', preco: 18.99, fragil: false},
    
]

console.log(produtos.filter((p) => p.preco > 500 && p.fragil))

const caro = produtos.filter((p) => p.preco > 500)
console.log(caro)

const fragil = produtos.filter((p) => p.fragil)
console.log(fragil)