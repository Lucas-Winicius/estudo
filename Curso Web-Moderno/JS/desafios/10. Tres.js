const divisorDeTres = (n) => {
    n = Number(n)
    if(n % 3 == 0) {
        return true
    } else {
        return false
    }
}

console.log(divisorDeTres(12))