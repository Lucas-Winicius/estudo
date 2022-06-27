const carrinho = [
    '{"nome": "Borracha", "preco": 3.45}',
    '{"nome": "Caderno", "preco": 13.90}',
    '{"nome": "Kit De Lapis", "preco": 41.22}',
    '{"nome": "Caneta", "preco": 7.5}',
]

let resultado = carrinho.map((e) => JSON.parse(e)).map((e) => e.preco)

console.log(resultado)