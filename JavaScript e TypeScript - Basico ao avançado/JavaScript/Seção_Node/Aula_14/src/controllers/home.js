exports.get = (req, res, next) => {
  req.flash('info', 'Information')
  req.flash('error', 'Error')
  req.flash('success', 'Success')
  res.render('index');
  next();
};

exports.post = (req, res) => res.send(`Hello, ${req.body.name}!`);
