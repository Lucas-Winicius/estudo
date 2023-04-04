require('dotenv').config()
const express = require('express');
const app = express();
const mongoose = require('mongoose');
mongoose
  .connect(
    process.env.MONGO_URL
  )
  .then(() => {
    app.emit('connect');
    console.log('Connected to mongodb');
  })
  .catch((err) => {
    console.error(err);
  });

const routes = require('./routes');
const path = require('path');
const meuMiddleware = require('./src/middlewares/middleware');

app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.resolve(__dirname, 'public')));
app.use(meuMiddleware);

app.set('views', path.resolve(__dirname, 'src', 'views'));
app.set('view engine', 'ejs');

app.use(routes);

app.on('connect', () => {
  app.listen(3000, () => {
    console.log('Acessar: http://localhost:3000');
    console.log('Servidor iniciado!');
  });
});
