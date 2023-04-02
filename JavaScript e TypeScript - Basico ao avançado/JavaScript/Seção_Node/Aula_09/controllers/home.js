exports.get = (req, res) => res.send(`Hello, World!`);

exports.post = (req, res) => res.send(`Hello, ${req.body.name}!`);
