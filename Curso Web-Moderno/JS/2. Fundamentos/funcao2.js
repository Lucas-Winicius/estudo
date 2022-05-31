// ARMAZENANDO UMA FUNÇAO DENTRO DE UMA VARIAVEL
const imprimirSoma = function (a, b) {
    console.log(a + b)
}

imprimirSoma(2, 3)

// ARMAZENANDO UMA FUNÇÃO ARROW EM UMA VARIAVEL
const soma = (a, b) => {
    return a + b
}

console.log(soma(2, 3))

// RETORNO IMPLICITO
const sub = (a, b) => a - b

console.log(sub(7, 2))

const imprimir2 = a => console.log(a)

imprimir2('5')