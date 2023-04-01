const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send(`
    <form action="/" method="POST">
        Nome: <input type="text" name="nome"/>
        <button type="submit">ENVIAR</button>
    </form>
    `);
})

app.post('/', (req, res) => {
    res.send(`RECEBI O POST`);
})

app.get('/contato', (req, res) => {
    res.send('Contato');
})

app.get('/:page', (req, res) => {
    res.send('Pagina não encontrada!');
})

app.listen(3000, () => {
    console.log('Acessar: http://localhost:3000');
    console.log('Servidor iniciado!')
})
