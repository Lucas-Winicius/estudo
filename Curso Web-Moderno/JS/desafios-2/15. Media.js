const calcularMedia = arrayc => console.log(arrayc.reduce((Acumulador, valorAtual) => Acumulador + valorAtual) / arrayc.length)

calcularMedia([0, 10]) // retornará 5
calcularMedia([1, 2, 3, 4, 5]) // retornará 3