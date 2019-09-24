#!/usr/bin/node
const request = require('request');

function printPeople (people, index) {
  if (index >= people.length) {
    return;
  }
  request(people[index], function (err, resp, body) {
    if (err) console.log(err);
    else {
      console.log(JSON.parse(body).name);
      return printPeople(people, index + 1);
    }
  });
}

request('https://swapi.co/api/films/' + process.argv[2], function (error, response, body) {
  if (error) console.log(error);
  const film = JSON.parse(body);
  const characters = film.characters;
  printPeople(characters, 0);
});
