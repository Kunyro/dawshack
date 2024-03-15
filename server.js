import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';

const http = require('node:http');
const bootstrap = require('bootstrap')

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello, World!\n');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

app.get("/showfile", (req, res, next) => { 
    // show the page
       const __filename = fileURLToPath(import.meta.url);
    const __dirname = path.dirname(__filename);
    const _retfile = path.join(__dirname, 'test.html');
   
    res.sendFile(_retfile);
   });