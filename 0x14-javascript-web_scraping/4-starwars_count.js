#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present

const request = require('request');
const URL = process.argv[2];
let films;
let counter = 0;

request({
  url: URL,
  json: true
}, function (error, response, body) {
  if (error) {
    console.log(error);
  }

  films = body.results;

  for (let i = 0; i < films.length; i++) {
    for (let j = 0; j < films[i].characters.length; j++) {
      if (films[i].characters[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
        counter++;
      }
    }
  }
  console.log(counter);
});
