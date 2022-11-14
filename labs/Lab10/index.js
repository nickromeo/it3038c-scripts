var express = require('express')
var app = express()
const config = require('config')
const { response } = require('express')
const fs = require('fs')


app.set('port', (process.env.PORT || 5000))
app.use(express.static(__dirname + '/public'))

app.get('/', function(request, response) {
  response.send('<b>Hello World! My name is:<em>' + process.env.MYNAME + '</em> <br/> My Node Enviroment is:<em>' + config.util.getEnv('NODE_ENV') + '</em><br> <a href="/api">Get Widgets</a></b>')
})

app.get('/api', (request, response) => {
    fs.readFile("./public/widgets.json", "UTF-8", (err, body) => {
            res.writeHead(200, {"Content-Type": "text/JSON"})
            res.end(body)
    })
})

app.listen(app.get('port'), function() {
  console.log("Node app is running at localhost:" + app.get('port'))
})
