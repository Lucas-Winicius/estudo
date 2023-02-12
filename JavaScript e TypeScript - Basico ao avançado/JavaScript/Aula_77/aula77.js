function CPF(cpf) {
  this.cpf = cpf;
  this.cpfLimpo = this.cpf.replace(/\D+/g, '');
  this.cpfArray = Array.from(this.cpfLimpo);

  this.primeiroDigito = () => {
    // REMOVE OS ULTIMOS 2 DIGITOS
    const semDigitosFinais = this.cpfArray.slice(0, -2);

    // FAZ A MATEMATICA NECESSARIA
    const multiplicacao = semDigitosFinais.map(
      (numero, index) => parseInt(numero) * (10 - index)
    );

    // SOMA TODOS OS NUMEROS
    const soma = multiplicacao.reduce(
      (acumulador, numero) => acumulador + numero,
      0
    );

    const primeiroDigito = 11 - (soma % 11);

    return primeiroDigito > 9 ? 0 : primeiroDigito;
  };

  this.segundoDigito = () => {
    const primeiroDigito = this.primeiroDigito();
    const semDigitosFinais = this.cpfArray.slice(0, -2);
    semDigitosFinais.push(primeiroDigito);

    const multiplicacao = semDigitosFinais.map(
      (numero, index) => parseInt(numero) * (11 - index)
    );

    const soma = multiplicacao.reduce(
      (acumulador, numero) => acumulador + numero,
      0
    );

    const segundoDigito = 11 - (soma % 11);

    return segundoDigito > 9 ? 0 : segundoDigito;
  };

  this.validar = () => {
    const primeiroDigito = this.primeiroDigito();
    const segundoDigito = this.segundoDigito();
    const semDigitosFinais = this.cpfArray.slice(0, -2);
    semDigitosFinais.splice(
      semDigitosFinais.length,
      0,
      primeiroDigito,
      segundoDigito
    );

    const cpfFinal = semDigitosFinais.join('');

    return cpfFinal === this.cpfLimpo;
  };
}

const c1 = new CPF('633.666.571-20');
console.log(c1.validar());