const express = require('express');
const app = express();
const bodyParser = require('body-parser')
const saudacao = require('./saudaçãoMid')
const usuarioAPI = require('./api/usuario')


app.use(bodyParser.text())
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }))
app.use(saudacao('Lucas W.'))

app.use('/hours', (req, res) => {
    res.send(new Date())
})

app.get('/json', (req, res) => {
    res.json({
        nome: 'Lucas',
        sobrenome: 'Winicius',
        idade: 16
    })
})

app.get('/array', (req, res) => {
    res.json([
        { nome: 'Lucas', sobrenome: 'Winicius', idade: 16 },
        { nome: 'Leonel', sobrenome: 'Soares', idade: 16 },
    ])
})

app.use('/middleware1', (req, res, next) => {
    console.log('Antes ...')
    next()
})

app.use('/middleware1', (req, res, next) => {
    console.log('Durante...')
    res.json({
        status: 200
    })
    next()
})

// O ultimo nao é necessario
app.use('/middleware1', (req, res, next) => {
    console.log('Depois...')
    // next()
})

app.get('/clientes/relatorio', (req, res) => {
    res.send(`Cliente relatorio: completo = ${req.query.completo} ano = ${req.query.ano}`)
})

app.get('/clientes/:id', (req, res) => {
    res.send(`Client ${req.params.id} selecionado!`)
})

app.post('/corpo', (req, res) => {
    // let corpo = ''
    // req.on('data', data => {
    //     corpo += data
    // })

    // req.on('end', () => res.send(corpo))

    res.send(req.body)
})

app.post('/usuario', usuarioAPI.salvar)
app.get('/usuario', usuarioAPI.obter)

require('./api/produto')(app, 'Meu Param')

app.listen(3000, console.log('\n\n - Executando na porta 3000.\n\n - http://localhost:3000\n\n'))