#!/usr/bin/node
// script that prints My number: <first argument converted in integer>

if (Number.isInteger(parseInt(process.argv[2]))) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
