let num = [1, 2, 3, 4, 5, 6, 7, 8, 9]//, 'Opa']
num.push(0)

/*
console.log(`Nosso Vetor E ${num}`)
console.log(`O vetor tem ${num.length} Posições.`)
console.log(num[2])
console.log(`Em Ordem Cresente: ${num.sort()}`)

for(let pos=0; pos<num.length; pos++) {
    console.log(num[pos])
}

// OU
console.log('OU')

for(let pos in num) {
    console.log(num[pos])
}
*/

let pos = num.indexOf('Opa')
console.log(`Opa esta na posição ${pos}`)

if(pos == -1) {
    console.log('Opa não esta nesta lista :/')
}