type Idade = number;
type RGB = "Vermelho" | "Verde" | "Blue";
type CMYK = "Ciano" | "Magenta" | "Amarelo" | "Preto";
type Cores = RGB | CMYK;

type Pessoa = {
  nome: string;
  peso: number;
  idade: Idade;
  corPreferida?: Cores;
};

const pessoa: Pessoa = {
  nome: "Lucas W.",
  peso: 60,
  idade: 16,
};

console.log(pessoa);

export default 1;
