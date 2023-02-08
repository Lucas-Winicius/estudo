function Produto(nome, preco) {
  this.nome = nome;
  this.preco = preco;
}

Produto.prototype.desconto = function (desconto) {
  this.preco = this.preco - this.preco * (desconto / 100);
};

Produto.prototype.aumento = function (aumento) {
  this.preco = this.preco + this.preco * (aumento / 100);
};

const p1 = new Produto('Caneta Azul', 1.5);
p1.desconto(10)
p1.aumento(100);
console.log(p1);
