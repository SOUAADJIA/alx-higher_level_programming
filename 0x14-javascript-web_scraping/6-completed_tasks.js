#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  const todos = JSON.parse(body);

  const completedTasksByUser = {};

  todos.forEach(todo => {
    if (todo.completed) {
      // Increment the count of completed tasks for the user
      completedTasksByUser[todo.userId] = (completedTasksByUser[todo.userId] || 0) + 1;
    }
  });

  console.log(completedTasksByUser);
});

