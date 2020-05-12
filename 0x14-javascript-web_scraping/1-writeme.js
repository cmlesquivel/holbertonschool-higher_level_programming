#!/usr/bin/node
// script that writes a string to a file

const fs = require('fs');

const myFile = process.argv[2];
const data = process.argv[3];

fs.writeFile(myFile, data, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }
});
