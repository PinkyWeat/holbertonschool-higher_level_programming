#!/usr/bin/node
const fs = require('fs'); // NODE.js built-in module
const args = process.argv;
const data = args[3];

fs.writeFile(args[2], data, 'utf-8', (err) => {
    if (err) {
        return console.log(err);
    }
});