#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

const characterId = '18';

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  // Count the occurrences of the character ID in the response body
  const characterCount = body.split(`/people/${characterId}/`).length - 1;

  console.log(characterCount);
});
