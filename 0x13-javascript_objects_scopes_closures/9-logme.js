#!/usr/bin/node
// function that returns the reversed version of a list
let counter = 0;

exports.logMe = function (item) {
  console.log(counter + ': ' + item);
  counter++;
};
