#!/usr/bin/node
// script that reads and prints the content of a file

const fs = require('fs');

const myFile = process.argv[2];

fs.readFile(myFile, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
