exports.get = (req, res, next) => {
  res.render('index');
  next();
};

exports.post = (req, res) => res.send(`Hello, ${req.body.name}!`);
