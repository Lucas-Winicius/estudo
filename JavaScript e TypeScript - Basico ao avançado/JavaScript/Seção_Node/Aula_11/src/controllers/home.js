exports.get = (req, res) => res.render('index');

exports.post = (req, res) => res.send(`Hello, ${req.body.name}!`);
