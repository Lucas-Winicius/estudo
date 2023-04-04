module.exports = (req, res, next) => {
  console.log('Middlewar GLOBAL');

  if (req.body.username) console.log('CADASTRANDO...');

  next();
};
