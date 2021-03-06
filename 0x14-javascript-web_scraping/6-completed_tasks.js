#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];
const tasks = {};

request(URL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const list = JSON.parse(body);
    for (const user of list) {
      if (user.completed === true) {
        const idToAdd = user.userId;
        if (!tasks[idToAdd]) {
          tasks[idToAdd] = 1;
        } else {
          tasks[idToAdd] += 1;
        }
      }
    }
    console.log(tasks);
  }
});
