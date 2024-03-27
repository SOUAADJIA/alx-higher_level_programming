#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movieData = JSON.parse(body);
  const charactersUrls = movieData.characters;

  const fetchCharacter = (characterUrl) => {
    return new Promise((resolve, reject) => {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      });
    });
  };

  Promise.all(charactersUrls.map(fetchCharacter))
    .then(characters => {
      characters.forEach(character => console.log(character));
    })
    .catch(error => {
      console.error(error);
    });
});
