#!/usr/bin/node

const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

const characterId = '18';

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  const data = JSON.parse(body);

  let movieCount = 0;

  // Iterate through each movie
  data.results.forEach(movie => {
    // Check if Wedge Antilles is present in the characters array
    if (movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
      movieCount++;
    }
  });

  console.log(movieCount);
});
