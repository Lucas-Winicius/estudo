const somarNumeros = (arrayc) => console.log(arrayc.reduce((Acumulador, ValorAtual) => Acumulador + ValorAtual))

somarNumeros([10, 10, 10]) // retornarĂ¡ 30
somarNumeros([15, 15, 15, 15]) // retornarĂ¡ 60