#!/usr/bin/node
// script that prints the add two: first and second argument passed to it

const myArray = [];
const lenArgv = process.argv.length;

if (lenArgv > 3) {
  for (let i = 2; i < lenArgv; i++) {
    myArray.push(process.argv[i]);
  }
  myArray.sort(function (a, b) {
    return a - b;
  });
  console.log(myArray[myArray.length - 2]);
} else {
  console.log('0');
}
