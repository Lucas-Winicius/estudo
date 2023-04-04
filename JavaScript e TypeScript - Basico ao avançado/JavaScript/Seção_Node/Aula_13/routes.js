const express = require('express');
const route = express.Router();

const home = require('./src/controllers/home');
const user = require('./src/controllers/users');

function meuMiddleware(req, res, next) {
  req.session = { name: 'Lucas', age: 16 };
  console.log('Passei aq 08');
  next();
}

route.get('/', meuMiddleware, home.get, (req, res) => {
  console.log('Req finalizada');
  console.log(JSON.stringify(req.session))
});
route.post('/', home.post);

route.get('/users', user.get);
route.post('/users', user.post);

module.exports = route;
