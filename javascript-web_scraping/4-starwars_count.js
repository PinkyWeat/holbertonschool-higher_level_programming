#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/people/';
const urlChar = 'https://swapi-api.hbtn.io/api/people/18/';

request(url, function (err, response, body) {
  if (err) {
    throw err;
  } else {
    if (response.statusCode === 200) {
      const data = JSON.parse(body).results;
      let count = 0;
      for (let each of data) {
        for (let chars of each.characters) {
          if (urlChar === chars) {
            ++count;
          }
        }
      }
      return console.log(count);
    }
  }
});
