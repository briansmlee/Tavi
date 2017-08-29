# Trello power-up
# starting from flask tutorial...
# Flask-CORS: https://flask-cors.readthedocs.io/en/latest/
# 


from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # allow CORS for all domains on all routes


# var express = require('express');
# var cors = require('cors');
# var app = express();
# 
# // your manifest must have appropriate CORS headers, you could also use '*'
# app.use(cors({ origin: '*' }));
# 
# // http://expressjs.com/en/starter/static-files.html
# app.use(express.static('public'));
# 
# // http://expressjs.com/en/starter/basic-routing.html
# app.get("*", function (request, response) {
#   response.sendFile(__dirname + '/views/index.html');
# });
# 
# // listen for requests :)
# var listener = app.listen(process.env.PORT, function () {
#   console.log('Your app is listening on port ' + listener.address().port);
# });











