module.exports = (app, texto) => {
    function salvar(req, res, next) {
        res.send(`Produto > Salvar > ${texto}`)
    }
    function obter(req, res, next) {
        res.send(`Produto > obter > ${texto}`)
    }

    app.post('/produto', salvar)
    app.get('/produto', obter)
}