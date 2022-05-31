function randint(min, max) {
    const valor = Math.random() * (max - min) + min
    return Math.floor(valor)
}

let opc = -1

do {
    opc = randint(-1, 10)
    console.log(opc)
} while (opc != -1)