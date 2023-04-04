require('dotenv').config();
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const session = require('express-session');
const flash = require('connect-flash');
const MongoStore = require('connect-mongo');
const routes = require('./routes');
const path = require('path');
const meuMiddleware = require('./src/middlewares/middleware');

const sessionOptions = session({
  secret: process.env.SECRET,
  store: MongoStore.create({ mongoUrl: process.env.MONGO_URL }),
  resave: false,
  saveUninitialized: false,
  cookie: {
    maxAge: 1000 * 60 * 60 * 24 * 7,
    httpOnly: true,
  },
});

mongoose
  .connect(process.env.MONGO_URL)
  .then(() => {
    app.emit('connect');
    console.log('Connected to mongodb');
  })
  .catch((err) => {
    console.error(err);
  });

app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.resolve(__dirname, 'public')));
app.use(meuMiddleware);
app.use(sessionOptions);
app.use(flash());

app.set('views', path.resolve(__dirname, 'src', 'views'));
app.set('view engine', 'ejs');

app.use(routes);

app.on('connect', () => {
  app.listen(3000, () => {
    console.log('Acessar: http://localhost:3000');
    console.log('Servidor iniciado!');
  });
});
