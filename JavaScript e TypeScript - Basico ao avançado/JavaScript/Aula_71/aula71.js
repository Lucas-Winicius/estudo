function Produto(nome, preco, estoque) {
  this.nome = nome;
  this.preco = preco;
//   this.estoque = estoque;

  Object.defineProperty(this, 'estoque', {
    enumerable: true,    // Mostra a chave
    value: estoque,      // Valor
    writable: false,     // Pode alterar o valor
    configurable: false  // Configuravel ou "apagavel" ( DefineProperty )
  })

  Object.defineProperties(this, {
    nome: {
        enumerable: true,   // Mostra a chave
        value: nome,        // Valor
        writable: false,    // Pode alterar o valor
        configurable: true  // Configuravel ou "apagavel" ( DefineProperty )
    },
    preco: {
        enumerable: true,   // Mostra a chave
        value: preco,       // Valor
        writable: true,     // Pode alterar o valor
        configurable: true  // Configuravel ou "apagavel" ( DefineProperty )
    }
  })

}

const p1 = new Produto('Abobora', 20, 1)
console.log(p1)