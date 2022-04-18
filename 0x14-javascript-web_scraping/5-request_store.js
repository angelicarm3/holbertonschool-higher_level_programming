#!/usr/bin/node
const process = require('process');
const request = require('request');
const fs = require('fs');

request(String(process.argv[2]), function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(String(process.argv[3]), body, 'utf8', function (err, data) {
      if (err) {
        return console.log(err);
      }
    }
    );
  }
});
