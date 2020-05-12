#!/usr/bin/node
// script that reads and prints the content of a file

const fs = require('fs');

const myFile = process.argv[2];

fs.readFile(myFile, (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data.toString().trim());
});
