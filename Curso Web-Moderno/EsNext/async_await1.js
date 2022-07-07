function esperarPor(tempo) {
    return new Promise(resolve => {  
    setTimeout(() => resolve(), tempo)
})}

// esperarPor(2000)
//     .then(console.log('Executando promise 1'))
//     .then(esperarPor(2000))
//     .then(console.log('Executando promise 2'))
//     .then(esperarPor(2000))
//     .then(console.log('Executando promise 3'))

const retornarValor = () => {
    return new Promise(resolve => {
        setTimeout(() => resolve(13), 5000)
    })
}

const executar = async () => {

    let valor = await retornarValor()
    console.log(valor)

    await esperarPor(2000)
    console.log('Async/Await 1...')

    await esperarPor(2000)
    console.log('Async/Await 2...')

    await esperarPor(2000)
    console.log('Async/Await 3...')

    return 12345
}

executar().then(console.log)