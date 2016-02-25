var http = require('http');
 
function onRequest(request, response) {
    console.log('request received.');
    response.writeHead(200, {'Content-Type' : 'text/plain'});
	response.write("Hello world\n");
	var date = new Date();
	var hour = date.getHours();
	var min = date.getMinutes();
	response.write("Time is : "+hour+":"+min);
    response.end();
}
 
http.createServer(onRequest).listen(80);
 
console.log('server has started.');
