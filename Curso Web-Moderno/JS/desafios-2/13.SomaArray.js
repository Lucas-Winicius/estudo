const somarNumeros = (arrayc) => console.log(arrayc.reduce((Acumulador, ValorAtual) => Acumulador + ValorAtual))

somarNumeros([10, 10, 10]) // retornará 30
somarNumeros([15, 15, 15, 15]) // retornará 60