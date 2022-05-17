function impar_par(numeros) {

    let impar = []
    let par = []

    for(let c = 0; c <= parseInt(numeros.length)- 1; c++) {
           if (numeros[c] % 2 == 0) {
                par.push(numeros[c])
           }
           else {
                impar.push(numeros[c])
           }
    }

    console.log('IMPARES: ' + impar)
    console.log('PARES: ' + par)

}

impar_par([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 203])
console.log('')
impar_par([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
console.log('')
impar_par([2, 6, 5, 5, 7, 44, ])
console.log('')
impar_par([15, 74, 66, 9, 45, 12, ])

