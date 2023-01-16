function salvar(req, res, next) {
    res.send('Usuario > Salvar')
}

function obter(req, res, next) {
    res.send('Usuario > Obter')
}

module.exports = { salvar, obter }