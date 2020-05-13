#!/usr/bin/node
// Script that display the status code of a GET request

const request = require('request');
const URL = process.argv[2];

request(URL, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log('code:', response && response.statusCode);
});
