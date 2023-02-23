const falar = {
  falar() {
    console.log(`${this.nome} esta falando`);
  },
};

const comer = {
  comer() {
    console.log(`${this.nome} esta comendo`);
  },
};

const beber = {
  beber() {
    console.log(`${this.nome} esta bebendo`);
  },
};

// const pessoaProto = Object.assign({ ...falar, ...comer, ...beber})
const pessoaProto = Object.assign({}, falar, comer, beber);

function criaPessoa(nome, sobrenome) { 

  return Object.create(pessoaProto, {
    nome: {
      value: nome,
    },
    sobrenome: {
      value: sobrenome,
    },
  });
}

const p1 = criaPessoa('Lucas', 'Winicius');
const p2 = criaPessoa('Maria', 'E.');
