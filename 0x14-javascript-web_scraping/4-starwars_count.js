#!/usr/bin/node

const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Character ID for Wedge Antilles
const characterId = '18';

// Make a GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  // Check for errors
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response
  const data = JSON.parse(body);

  // Initialize a counter for movies with Wedge Antilles
  let movieCount = 0;

  // Iterate through each movie
  data.results.forEach(movie => {
    // Check if Wedge Antilles is present in the characters array
    if (movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
      movieCount++;
    }
  });

  // Print the number of movies with Wedge Antilles
  console.log(movieCount);
});
