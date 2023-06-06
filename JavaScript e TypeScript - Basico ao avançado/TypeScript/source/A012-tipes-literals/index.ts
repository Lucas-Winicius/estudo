/* eslint-disable */
let x = 10;
x = 0b1010;
const y = 10;
let a: 100 = 100;
let b = 100 as const;
const c = 100 as const;

const pessoa = {
  nome: "Lucas" as const,
  sobrenome: "Winicius",
};

function cor(c: "Blue" | "Red" | "Green" | "Yellow" | "Black" | "Purple"): string {
  return c;
}

console.log(cor("Black"))

export default 1;
