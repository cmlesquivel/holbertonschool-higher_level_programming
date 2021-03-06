#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');
const URL = process.argv[2];
const myFile = process.argv[3];

request({
  url: URL
}, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(myFile, body, 'utf8', (err, data) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
