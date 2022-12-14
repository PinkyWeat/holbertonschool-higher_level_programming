#!/usr/bin/node
const request = require('request');
// const url = 'https://swapi-api.hbtn.io/api/films/';
const id = 18;

request('https://swapi-api.hbtn.io/api/films/' + id, function (err, response, body) {
  if (err) {
    return console.log(err);
  } else {
    if (response.statusCode === 200) {
      const data = JSON.parse(body);
      let count = 0;
      for (data.title of data) {
        count += 1;
      }
      console.log(count);
      return count;
    }
  }
});
