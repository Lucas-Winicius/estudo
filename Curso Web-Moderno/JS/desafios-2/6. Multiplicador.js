const multiplicar = (a = 1, b = 1) => {
    if(Number(a) >= 0 && Number(b) >= 0) {
        console.log(`${a} X ${b} = ${a * b}`)
    } else {
        console.log('Erro!')
    }
}

multiplicar(0, 0)
multiplicar(0, 1)
multiplicar(4, 1)
multiplicar(-4, 1)
multiplicar(4, -1)
multiplicar(4, 4)
multiplicar(5)