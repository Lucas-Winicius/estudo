const random = (min, max) => Math.floor(Math.random() * (max - min)) + min;

function esperaAi(msg, tempo) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (typeof msg !== 'string') {
        reject('Cai no erro!');
        return;
      }
      resolve(msg); // Valor unico
    }, tempo);
  });
}

const promisses = [
  'Primeiro valor',
  esperaAi('Promisse 1', 3000),
  esperaAi('Promisse 2', 500),
  esperaAi('Promisse 3', 1000),
  esperaAi(1000, 1000),
  'Outro valor',
];

// Resolve todas ou somente o erro
/* Promise.all(promisses)
  .then((valor) => console.log(valor))
  .catch((e) => console.log(e));
*/

// Primeiro valor retornado
/* Promise.race(promisses)
  .then((valor) => console.log(valor))
  .catch((e) => console.log(e));
*/

function baixaPagina() {
  const emCache = true;

  if (emCache) {
    // return Promise.resolve('Pagina em cache');
    return Promise.reject('Pagina ja em cache');
  } else {
    return esperaAi('Baixei', random(1000, 4000));
  }
}

baixaPagina()
  .then((valor) => console.log(valor))
  .catch((e) => console.log(e));
