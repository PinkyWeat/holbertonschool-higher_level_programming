#!/usr/bin/node
const request = require('request');
// const url = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];

request('https://swapi-api.hbtn.io/api/films/' + id, function (err, response, body) {
  if (err) {
    return console.log(err);
  } else {
    if (response.statusCode === 200) {
      console.log(JSON.parse(body).title);
    }
  }
});
