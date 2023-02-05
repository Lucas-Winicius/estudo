function* contador() {
    let i = 0
    while(true) {
        yield i
        i++
    }
}

const c = contador()
console.log(c.next().value)
console.log(c.next().value)
console.log(c.next().value)

// for(let v of c) {
//     console.log(v)
// }