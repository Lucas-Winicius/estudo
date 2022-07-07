// setTimeout(() => {
//     console.log('Executando callback...')
    
//     setTimeout(() => {
//         console.log('Executando callback...')
        
//         setTimeout(() => {
//             console.log('Executando callback...')

//         }, 2000)
//     }, 2000)
// }, 2000)

const esperarPor = (tempo = 2000) => new Promise((resolve, reject) => {
    setTimeout(() => {
        console.log('Resolvendo...')
        resolve('Resolvido!!')
    }, tempo)
})

// esperarPor(3000).then(retorno => console.log(retorno))
esperarPor().then(esperarPor()).then(esperarPor())