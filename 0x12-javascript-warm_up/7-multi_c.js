#!/usr/bin/node
// script that prints x times “C is fun”

const myVar = parseInt(process.argv[2]);

if (Number.isInteger(myVar)) {
  if (myVar > 0) {
    for (let i = 0; i < myVar; i++) {
      console.log('C is fun');
    }
  }
} else {
  console.log('Missing number of occurrences');
}
