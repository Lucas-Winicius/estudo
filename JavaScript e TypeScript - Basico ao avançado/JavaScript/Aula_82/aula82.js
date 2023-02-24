const _velocidade = Symbol('velocidade');
class Carro {
    constructor(nome) {
        this.nome = nome;
        this[_velocidade] = 0;
    }

  set velocidade(valor) {
    if(typeof valor !== 'number') return;
    if(valor <= 0 || valor >= 100) return;
    this[_velocidade] = valor;
  }

  get velocidade() {
    return this[_velocidade];
  }

  acelerar() {
    if (this[_velocidade] >= 100) return;
    this[_velocidade]++;
  }

  freiar() {
    if (this[_velocidade] <= 0) return;
    this[_velocidade]++;
  }
}

const c1 = new Carro('Skyline');
for (let i = 0; i < 55; i++) c1.acelerar();

console.log(c1);
