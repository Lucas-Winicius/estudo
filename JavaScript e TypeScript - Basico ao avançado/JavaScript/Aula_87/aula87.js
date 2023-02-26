const random = (min, max) => Math.floor(Math.random() * (max - min)) + min;

function esperaAi(msg, tempo) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(msg); // Valor unico
    }, tempo);
  });
}

esperaAi('Frase 1', random(1000, 5000))
  .then((res) => {
    console.log(res);
    return esperaAi('Frase 2', random(1000, 5000));
  })
  .then((res) => {
    console.log(res);
    return esperaAi('Frase 3', random(1000, 5000));
  })
  .then((res) => console.log(res))
  .catch((err) => console.error(err));
