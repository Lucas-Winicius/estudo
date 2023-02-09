function Produto(nome, preco) {
  this.nome = nome;
  this.preco = preco;
}

Produto.prototype.aumento = function (aumento) {
  this.preco += aumento;
};

Produto.prototype.desconto = function (desconto) {
  this.preco -= desconto;
};

// -------------------------------------------------------------------

function Camiseta(nome, preco, cor) {
  Produto.call(this, nome, preco);
  this.cor = cor;
}

Camiseta.prototype = Object.create(Produto.prototype);
Camiseta.prototype.constructor = Camiseta;

Camiseta.prototype.aumento = function (aumento) {
  this.preco = this.preco + this.preco * (aumento / 100);
};

// -------------------------------------------------------------------

function Caneca(nome, preco, material) {
  Produto.call(this, nome, preco);
  this.material = material;
}

Caneca.prototype = Object.create(Produto.prototype);
Caneca.prototype.constructor = Caneca;

// -------------------------------------------------------------------

const c1 = new Caneca('Caneco', 20, 'Plastico');
c1.aumento(80);
console.log(c1);
 