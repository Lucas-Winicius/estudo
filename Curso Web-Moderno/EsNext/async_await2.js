const randint = (min, max, numerosProibidos) => {
    if (min > max) {
        [max, min] = [min, max]
    }

    return new Promise((resolve, reject) => {
        const aleatorio = parseInt(Math.random() * (max - min + 1)) + min

        if(numerosProibidos.includes(aleatorio)) {
            reject('Numero Repitido!')
        } else {
            resolve(aleatorio)
        }
    })
}

const gerarMegaSena = async (qntDeNumeros) => {

    try {
        const numeros = []
        for(let _ of Array(qntDeNumeros).fill()) {
            numeros.push(await randint(1, 60, numeros))
        }
    
        return numeros
        
    } catch (e) {
        throw 'Que chato'
    }

}

gerarMegaSena(10)
    .then(console.log)
    .catch(console.log)