const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');

var free_memory = os.freemem();
var free_mem_in_mb = free_memory/1000000;


var total_memory = os.totalmem();
var total_mem_in_mb = total_memory/1000000;



var ut_sec = os.uptime();
var ut_min = ut_sec/60;
var ut_hour = ut_min/60;
   
ut_sec = Math.floor(ut_sec);
ut_min = Math.floor(ut_min);
ut_hour = Math.floor(ut_hour);
  
ut_hour = ut_hour%60;
ut_min = ut_min%60;
ut_sec = ut_sec%60;

var cpu_s=os.cpus();
var no_of_logical_core=0;
cpu_s.forEach(element => { 
    no_of_logical_core++;
}); 


http.createServer((req, res) => {
    myHostName=os.hostname();
    html=`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Nick Romeo Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
        <p>Server Uptime: ${ut_hour} hours ${ut_min} minutes and ${ut_sec} seconds </p>
        <p>Total Memory: ${total_mem_in_mb} MBs </p>
        <p>Free Memory: ${free_mem_in_mb} MBs</p>
        <p>Number of CPUs: ${no_of_logical_core} </p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
}).listen(3000);

console.log("Server listening on port 3000");