function criaErro(): never {
  throw new Error("erro!");
}

// trava o code, lança erro, loop, etc...
criaErro();
