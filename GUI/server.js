let express = require('express')
let app = express()
let server = app.listen(3000, () => {
    console.log('server started at localhost:3000')
})
app.use(express.static('public'))
