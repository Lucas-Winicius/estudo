function randint(min, max) {
    const valor = Math.random() * (max - min) + min
    return Math.floor(valor)
}

let opc = 0

while (opc != -1) {
    opc = randint(-1, 1000)
    console.log(opc)
}