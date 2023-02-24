const pessoas = [
  { id: 2, nome: 'Lucas' },
  { id: 3, nome: 'Leo' },
  { id: 1, nome: 'Maria' },
  { id: 4, nome: 'Pedro' },
];

// const novasPessoas = {}
// for(let pessoa of pessoas) {
//     const { id } = pessoa;
//     novasPessoas[id] = pessoa;
// }

const novasPessoas = new Map();
for (let pessoa of pessoas) {
  const { id } = pessoa;
  novasPessoas.set(id, { ...pessoa });
}

console.log(novasPessoas);
console.log(novasPessoas.get(3));

// for(let pessoa of novasPessoas) {
//     console.log(pessoa)
// }

for(let [identifier, {id, nome}] of novasPessoas) {
    console.log(identifier, id, nome)
}