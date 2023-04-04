exports.get = (req, res) => res.send('Listando usuarios...');

exports.post = (req, res) => res.send(`Salvando dados: <br/>Usuario: ${req.body.username}<br />Senha: ${req.body.password}`)