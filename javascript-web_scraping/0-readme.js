#!/usr/bin/node
const fs = require('fs'); // NODE.js built-in module
let args = process.argv;

fs.readFile(args[2], 'utf8', (err, data)=>{
    if(err) {
        return console.log(err);
    }
    console.log(data);
});
