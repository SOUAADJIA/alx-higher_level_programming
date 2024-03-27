#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (!err) {
    const tasksData = JSON.parse(body);
    const completedTasksByUser = {};
    tasksData.forEach(task => {
      if (task.completed) {
        if (!(task.userId in completedTasksByUser)) {
          completedTasksByUser[task.userId] = 1;
        } else {
          completedTasksByUser[task.userId] += 1;
        }
      }
    });
    console.log(completedTasksByUser);
  } else {
    console.error(err);
  }
});
