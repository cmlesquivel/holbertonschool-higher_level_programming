#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');
const URL = process.argv[2];
const myFile = process.argv[3];

request({
  url: URL,
  json: true
}, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(myFile, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
