// novo recurso do ES2015

const pessoa = {
    nome: 'Ana',
    idade: 5,
    endereco: {
        logadouro: 'Rua ABC',
        numero: 1000
    }
}

const { nome, idade  } = pessoa
console.log(nome, idade)

const {nome: n, idade: i} = pessoa
console.log(n, i)

const {nome: nom} = pessoa
console.log(nom)

const {sobreNome, bemHumorado = true} = pessoa
console.log(sobreNome, bemHumorado)

const {endereco} = pessoa
console.log(endereco)

const { endereco: {logadouro, numero, cep = "00000000"}} = pessoa
console.log(logadouro, numero, cep)