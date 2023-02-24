class DispositivoEletronico {
  constructor(nome, novo) {
    this.nome = nome;
    this.novo = novo;
    this.ligado = false;
  }

  ligar() {
    if (this.ligado) {
      console.log(this.nome + ' Ja ligado.');
      return;
    }
    this.ligado = true;
  }

  desligar() {
    if (!this.ligado) {
      console.log(this.nome + ' Ja desligado.');
      return;
    }
    this.ligado = false;
  }
}

class Smartphone extends DispositivoEletronico {
  constructor(nome, cor, modelo, novo) {
    super(nome, novo);

    this.cor = cor;
    this.modelo = modelo;
  }
}

const s1 = new Smartphone('Samsung', 'Azul Marinho', 'Galaxy S10', true);
console.log(s1);
