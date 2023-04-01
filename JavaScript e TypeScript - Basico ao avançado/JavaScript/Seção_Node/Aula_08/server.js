const express = require('express');
const app = express();

app.use(express.urlencoded({ extended: true }))

app.get('/', (req, res) => {
    res.send(`
    <form action="/" method="POST">
        Nome: <input type="text" name="nome"/>
        Sobrenome: <input type="text" name="sobrenome"/>
        <button type="submit">ENVIAR</button>
    </form>
    `);
})

app.get('/testes/:usuarios?/:paramOPC?', (req, res) => {
    console.log(req)
    res.send('Buscando usuario: ' + JSON.stringify(req.query))
})

app.post('/', (req, res) => {
    console.log(req.body)
    res.send(`RECEBI O POST`);
})

app.get('/contato', (req, res) => {
    res.send('Contato');
})

app.listen(3000, () => {
    console.log('Acessar: http://localhost:3000');
    console.log('Servidor iniciado!')
})
