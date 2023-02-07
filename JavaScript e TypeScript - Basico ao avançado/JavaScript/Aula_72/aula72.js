function Produto(nome, preco, estoque) {
  this.nome = nome;
  this.preco = preco;
  let estoquePrivado = estoque

  Object.defineProperty(this, 'estoque', {
    enumerable: true,    // Mostra a chave
    // value: estoque,      // Valor
    // writable: false,     // Pode alterar o valor
    configurable: false,  // Configuravel ou "apagavel" ( DefineProperty )
    get: function() {
      return estoquePrivado
    },
    set: function(value) {
      if(typeof value !== 'number') {
        throw new TypeError('Use apenas numeros')
      }

      estoquePrivado = value
    }
  })



}

const p1 = new Produto('Abobora', 20, 1)
p1.estoque = 500
console.log(p1.estoque)