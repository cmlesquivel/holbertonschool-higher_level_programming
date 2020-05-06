#!/usr/bin/node
// script that prints the add two: first and second argument passed to it

const numberA = parseInt(process.argv[2]);
const numberB = parseInt(process.argv[3]);

if (Number.isInteger(numberA) && Number.isInteger(numberB)) {
  add(numberA, numberB);
} else {
  console.log('NaN');
}

function add (a, b) {
  console.log(a + b);
}
