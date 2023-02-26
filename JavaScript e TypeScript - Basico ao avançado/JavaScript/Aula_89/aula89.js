const random = (min = 0, max = 5000) =>
  Math.floor(Math.random() * (max - min)) + min;

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

async function executa() {
   // TRATAMENTO DE ERROS [ try - catch, ou .catch ]
  // apos o erro o code ira para o catch

  try {
    const fase1 = await esperaAi('Faze 1', random());
    console.log(fase1);

    const fase2 = await esperaAi('Faze 2', random());
    console.log(fase2);

    const fase3 = await esperaAi('Faze 3', random());
    console.log(fase3);
  } catch (e) {
    console.log(e);
  }
}

executa();
