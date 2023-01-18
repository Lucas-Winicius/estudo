const app = require('express')()
const consign = require('consign')

consign()
    .then('./config/middlewares.js')
    .into(app)

app.listen(3000, console.log('\n\n- Backend Iniciado.\n\n- Server: http://localhost:3000\n\n'))