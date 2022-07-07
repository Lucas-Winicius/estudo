const randint = (min, max, tempo = 1) => {
    if (min > max) {
        [max, min] = [min, max]
    }

    return new Promise((resolve, reject) => {

        setTimeout(() => {
            const aleatorio = parseInt(Math.random() * (max - min + 1)) + min
    
            if(aleatorio * 0 != 0) reject(-1)
            else resolve(aleatorio)

        }, tempo * 1000)

    })
}

function gerarVariosNumeros() {
    return Promise.all([
        randint(1, 60),
        randint(10, 600, 2),
        randint(80, 100, 5),
        randint(20, 100),
        randint(200, 500, 7),
        randint(200, 600, 8),
        randint(200, 600, 9),
        randint(200, 600, 4),
        randint(200, 600, 3)
    ])
}

gerarVariosNumeros().then(numeros => console.log(numeros))