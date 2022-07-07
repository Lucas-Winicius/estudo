// Criação e Promesa

const myPromise = new Promise((resolve, reject) => {

    const nome = "Luvas"

    if(nome === 'Luvas') {
        resolve('Usuario Lucas encontrado')
    } else {
        reject('O usuario Luvas não foi encontrado')
    }

})

myPromise.then((data) => {
    console.log(data)
}).catch(data => console.log(data))

// Encadeamento de Promise

const myPromise2 = new Promise((resolve, reject) => {

    const nome = "Luvas"

    if(nome === 'Luvas') {
        resolve('Usuario Lucas encontrado')
    } else {
        reject('O usuario Luvas não foi encontrado')
    }

})

myPromise2
    .then((data) => {return { data, err: -1, calendario: new Date() }})
    .then(obj => console.log(obj))
    .catch(data => console.log(data))

// Retorno do catch

const myPromise3 = new Promise((resolve, reject) => {

    const nome = "Lucas"

    if(nome === 'Luvas') {
        resolve('Usuario Lucas encontrado')
    } else {
        reject('O usuario Luvas não foi encontrado')
    }

})

myPromise3
    .then((data) => {return { data, erro: -1, calendario: new Date() }})
    .then(obj => console.log(obj))
    .catch(err => console.log('Houve um erro: ' + err))


// Resolver promesas Variadas
const p1 = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('P1 ok!')
    }, 5000)
})

const p2 = new Promise((resolve, reject) => {
    resolve('P2 ok!')
})

const p3 = new Promise((resolve, reject) => {
    resolve('P3 ok!')
})

const resolveAll = Promise.all([p1, p2, p3]).then(data => console.log(data))

const userName = "Lucas-Winicius"

fetch(`https://api.github.com/users/${userName}`, {
    method: 'GET',
    headers: {
        Accept: 'aplication/vnd.github.v3+json'
    }
}).then(data => data.json()).then(data => console.log(data)).catch(data => console.log(data))