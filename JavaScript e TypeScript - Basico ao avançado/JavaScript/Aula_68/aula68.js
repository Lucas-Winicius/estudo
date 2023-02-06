const numeros = [5, 50, 80, 1, 2, 3, 5, 8, 7, 11, 15, 22, 27];

const total = numeros
  .filter((numero) => numero % 2 === 0)
  .map((numero) => numero * 2)
  .reduce((acumulador, numero) => acumulador += numero);

console.log(total);
