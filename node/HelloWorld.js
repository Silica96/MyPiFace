var http = require('http');

function onRequest(request, response) {
  response.writeHead(200, {'Content-Type' : 'text/plain'});
  response.write('Hello World');
  a = 10;
  //response.write(a);
  response.end();
}
var date = new Date();
var current_hour = date.getHours();

http.createServer(onRequest).listen(8888);
