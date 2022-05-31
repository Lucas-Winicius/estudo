function rand([min = 0, max = 1000]) {
    if (min > max) [min, max] = [max, min]
    const valor = Math.random() * (max - min) + min
    return Math.floor(valor)
}



console.log(rand([2, 40]))
console.log(rand([40, 2]))
console.log(rand([40]))
console.log(rand([3]))
console.log(rand([, 6]))
console.log(rand([]))