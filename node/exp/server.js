var http = require('http');
var fs = require('fs');
var formidable = require("formidable");
var util = require('util');

var server = http.createServer(function (req, res) {
    if (req.method.toLowerCase() == 'get') {
        displayForm(res);
    } else if (req.method.toLowerCase() == 'post') {
        processFormFieldsIndividual(req, res);
    }
});

function displayForm(res) {
    fs.readFile('form.html', function (err, data) {
        res.writeHead(200, {
            'Content-Type': 'text/html',
                'Content-Length': data.length
        });
        res.write(data);
        res.end();
    });
    return;
}


function processFormFieldsIndividual(req, res) {
    var fields = [];
    var form = new formidable.IncomingForm();

    var fs = require('fs');

    var data;

    form.on('field', function (field, value) {
        console.log(value);
        fields[field] = value;
        data = value;
        fs.writeFile('text1.txt', value, 'utf8', function(error){
            console.log('write end')
        });
    });
    form.parse(req);
}

server.listen(1185);
console.log("server listening on 1185");
