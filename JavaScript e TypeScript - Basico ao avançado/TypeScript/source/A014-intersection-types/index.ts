type TemNome = { nome: string };
type TemSobrenome = { sobrenome: string };
type TemIdade = { idade: number };
type Pessoa = TemIdade & TemNome & TemSobrenome;

const pessoa: Pessoa = {
  nome: "Lucas",
  sobrenome: "Winicius",
  idade: 16,
};

type AB = "A" | "B";
type AC = "C" | "A";
// O QUE SE REPETE
type intercecao = AB & AC; // eslint-disable-line

export { pessoa };
