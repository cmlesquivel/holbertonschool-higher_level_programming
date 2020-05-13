#!/usr/bin/node
// Script that prints the title of a Star Wars movie

const request = require('request');
const movieId = process.argv[2];

const URL = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request({
  url: URL,
  json: true
}, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log(body.title);
});
