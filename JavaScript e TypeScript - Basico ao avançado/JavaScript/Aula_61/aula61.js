function* geradora1() {
    yield '1'
    yield '2'
    yield '3'
    yield '4'
    yield '5'
}

const g1 = geradora1()
console.log(g1.next().value)
console.log(g1.next().value)
console.log(g1.next().value)

console.log("# # # # # # # #")

for(let valor of g1) {
    console.log(valor)
}