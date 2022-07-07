const randint = (min, max) => {
    if (min > max) {
        [max, min] = [min, max]
    }

    return new Promise((resolve, reject) => {
        const aleatorio = parseInt(Math.random() * (max - min + 1)) + min

        if(aleatorio * 0 != 0) reject(-1)
        else resolve(aleatorio)
    })
}

const p = randint(10, 100).then(console.log).catch(console.log)