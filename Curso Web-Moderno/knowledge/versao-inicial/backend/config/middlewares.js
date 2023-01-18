import bodyParser from 'bodyParser'
import cors from 'cors'

module.exports = app => {
    app.use(bodyParser.json())
    app.use(cors())
}