function rand({min = 0, max = 1000}) {
    const valor = Math.random() * (max - min) + min
    return Math.floor(valor)
}

console.log(rand({min: 2, max: 40}))
console.log(rand({max: 40}))
console.log(rand({min: 3}))
console.log(rand({}))