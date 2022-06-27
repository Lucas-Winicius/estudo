Array.prototype.map2 = function(callback) {
    const newArray = []
    for(let i = 0; i < this.length; i++) {
        newArray.push(callback(this[i], i, this))
    }
    return newArray
}

const carrinho = [
    '{"nome": "Borracha", "preco": 3.45}',
    '{"nome": "Caderno", "preco": 13.90}',
    '{"nome": "Kit De Lapis", "preco": 41.22}',
    '{"nome": "Caneta", "preco": 7.5}',
]

let resultado = carrinho.map2((e) => JSON.parse(e)).map2((e) => e.preco)

console.log(resultado)