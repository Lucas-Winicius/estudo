enum Cores {
  VERMELHO, // 0
  AZUL, //     1
  AMARELO, //  2
}

console.log(Cores.VERMELHO);
console.log(Cores[0]);

function escolherCor(cor: Cores): void {
  console.log(Cores[cor]);
}

escolherCor(Cores.AZUL);
