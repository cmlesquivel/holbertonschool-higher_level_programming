#!/usr/bin/node
// Script that prints the title of a Star Wars movie

const request = require('request');
const movieId = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/' + movieId;
let films;

request({
  url: URL,
  json: true
}, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  films = body.characters;
  for (let i = 0; i < films.length; i++) {
    request({
      url: films[i],
      json: true
    }, function (error, response, body) {
      if (error) {
        console.log(error);
      } else {
        console.log(body.name);
      }
    });
  }
});
