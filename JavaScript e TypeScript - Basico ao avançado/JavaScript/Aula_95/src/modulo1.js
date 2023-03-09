const nome = 'Lucas';
const sobrenome = 'Winicius';
const idade = 16;

const url = 'https://google.com';

function soma(x, y) {
  return x + y;
}

export function sub(x, y) {
  return x - y;
}

export { nome, sobrenome, idade, soma, url as googleLink };

export default function data() {
  return Date.now();
}
