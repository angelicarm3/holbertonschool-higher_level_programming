#!/usr/bin/node
const request = require('request');
const requestURL = process.argv[2];

request(requestURL, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', response.statusCode);
  }
});
