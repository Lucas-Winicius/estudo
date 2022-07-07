const fs = require('fs')

const caminho = __dirname + '/arquivo.json'


// Sincrono...
const conteudo = fs.readFileSync(caminho, 'utf-8')
console.log(conteudo)

// Assincrono...
fs.readFile(caminho, 'utf-8', (err, conteudo) => {
    const informacao = JSON.parse(conteudo)
    console.log(informacao.nome)
})

const informacao = require('./arquivo.json')
console.log(informacao)

fs.readdir(__dirname, (err, arquivos) => {
    console.log('Conteudo Da Pasta...')
    console.log(arquivos)
})