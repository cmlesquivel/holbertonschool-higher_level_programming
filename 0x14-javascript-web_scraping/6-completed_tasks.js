#!/usr/bin/node
// script that computes the number of tasks completed by user id

const request = require('request');
const URL = process.argv[2];
const ids = {};
let userId;

request({
  url: URL,
  json: true
}, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    for (let j = 0; j < body.length; j++) {
      if (body[j].completed === true) {
        userId = body[j].userId.toString();
        typeof ids[userId] === 'undefined' ? ids[userId] = 1 : ids[userId] += 1;
      }
    }
  }
  console.log(ids);
}
);
