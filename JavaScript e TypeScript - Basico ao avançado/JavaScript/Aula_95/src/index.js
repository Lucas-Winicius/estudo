import { nome, sobrenome, idade, soma, googleLink, sub } from './modulo1';
import * as MyModule from './modulo1';
import qualQuerNome from './modulo1';

class Pessoa {
  constructor(nome, sobrenome, idade) {
    this.nome = nome;
    this.sobrenome = sobrenome;
    this.idade = idade;
  }

  dados() {
    return `
    Nome: ${this.nome}
    Sobrenome: ${this.sobrenome}
    Idade: ${this.idade}`;
  }
}

const p1 = new Pessoa(nome, sobrenome, idade);
const nomev = p1.dados();

console.log(nomev);
console.log(soma(10, 5));
console.log(googleLink);
console.log(sub(10, 5));
console.log(qualQuerNome());
