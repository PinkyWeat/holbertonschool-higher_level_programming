#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    return console.log(err);
  }
  console.log('code: ' + response.statusCode);
});

// https.get(url, (response) => {
// console.log('code: ', response.statusCode);
// }); Works in terminal just right, but I'm not using request.
