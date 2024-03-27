#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const data = JSON.parse(body);

  let characterIndex = 0;
  const fetchCharacter = () => {
    if (characterIndex < data.characters.length) {
      const characterUrl = data.characters[characterIndex++];
      request(characterUrl, (err, response, body) => {
        if (err) {
          console.error(err);
          return;
        }
        const characterData = JSON.parse(body);
        console.log(characterData.name);
        fetchCharacter();
      });
    }
  };

  fetchCharacter();
});
