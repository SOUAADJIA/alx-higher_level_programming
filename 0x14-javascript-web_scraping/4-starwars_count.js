#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  
  // Count the occurrences of '/people/18/' in the response body
  const count = (body.match(/\/people\/18\//g) || []).length;
  
  console.log(count);
});
