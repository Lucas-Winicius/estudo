function Pessoa(nome, sobrenome) {
  this.nome = nome;
  this.sobrenome = sobrenome;
  //   this.nomeCompleto = () => `${this.nome} ${this.sobrenome}`;
}

const pessoa1 = new Pessoa('Lucas', 'Winicius');

Pessoa.prototype.nomeCompleto = function () {
  return `${this.nome} ${this.sobrenome}`;
};

console.dir(pessoa1.nomeCompleto());
