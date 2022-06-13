let soma = (x, y) => x + y

let sub = (x, y) => x - y

let mult = (x, y) => x * y

let div = (x, y) => x / y

let painel = (x, y) => {
    console.log(`Soma: ${soma(x, y)}`)
    console.log(`Subtração: ${sub(x, y)}`)
    console.log(`Multiplicação: ${mult(x, y)}`)
    console.log(`Divisão: ${div(x, y)}`)
}

painel(1, 5)