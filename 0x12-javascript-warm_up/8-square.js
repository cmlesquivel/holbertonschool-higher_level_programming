#!/usr/bin/node
// script that prints a square

const myVar = parseInt(process.argv[2]);

if (Number.isInteger(myVar)) {
  if (myVar > 0) {
    for (let i = 0; i < myVar; i++) {
      console.log('X'.repeat(myVar));
    }
  }
} else {
  console.log('Missing size');
}
