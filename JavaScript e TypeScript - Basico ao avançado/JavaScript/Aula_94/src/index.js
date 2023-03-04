class Pessoa {
  constructor(nome, sobrenome) {
    this.nome = nome;
    this.sobrenome = sobrenome;
  }

  nome() {
    return `${this.nome} ${this.sobrenome}`;
  }
}

const p1 = new Pessoa('Lucas', 'Winicius');
const nome = p1.nome();
console.log(nome);
