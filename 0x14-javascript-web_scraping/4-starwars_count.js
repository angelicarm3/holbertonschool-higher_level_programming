#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];
const id = 18;
let counter = 0;

request(URL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    for (const movie of JSON.parse(body).results) {
      for (const character of movie.characters) {
        if (character.includes(id)) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
