const express = require('express');
const route = express.Router();

const home = require('./src/controllers/home');
const user = require('./src/controllers/users');

route.get('/', home.get);
route.post('/', home.post);

route.get('/users', user.get)
route.post('/users', user.post)

module.exports = route;
