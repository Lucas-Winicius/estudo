const soma = function(x, y) {
    return x + y
}

const imprimirReultado = function(a, b, operacao = soma) {
    console.log(operacao(a, b))
}

imprimirReultado(2, 5)
imprimirReultado(2, 5, soma)
imprimirReultado(2, 5, (x, y) => `Numero 1: ${x} Numero 2: ${y} Resultado: ${x+y}`)