#!/usr/bin/node
const request = require('request');
// const url = 'https://swapi-api.hbtn.io/api/films/';
const id = 18;

request('https://swapi-api.hbtn.io/api/films/' + id, function (err, response, body) {
  if (err) {
    return console.log(err + ' ' + response.statusCode);
  } else {
    if (response.statusCode === 200) {
      const data = JSON.parse(body).results;
      let count = 0;
      for (const each of data) {
        for (const chars of each.characters) {
          if (chars.endsWith('/18/')) {
            ++count;
          }
        }
      }
      console.log(count);
      return count;
    }
  }
});
