const randint = (min, max) => Math.floor(Math.random() * (max - min + 1) + min)

const funcaoDaSorte = (num) => {
    const numeroSorteado = randint(1, 10)
    if(Number(num) == numeroSorteado) {
        console.log(`Parabéns! O número sorteado foi o ${num}`)
    } else {
        console.log(`Que pena! O número sorteado foi o ${numeroSorteado} não o ${num}`)
    }
}


funcaoDaSorte(10) // retornará "Parabéns! O número sorteado foi o 10"
funcaoDaSorte(5) // retornará "Que pena! O número sorteado foi o 3"
funcaoDaSorte(5) // retornará "Que pena! O número sorteado foi o 1"