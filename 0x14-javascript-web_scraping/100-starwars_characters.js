#!/usr/bin/node
const request = require('request');
request('https://swapi.co/api/films/' + process.argv[2], function (error, response, body) {
  if (error) console.log(error);
  const film = JSON.parse(body);
  const chars = film.characters;
  for (let i = 0; i < chars.length; i++) {
    request(chars[i], function (err, resp, bdy) {
      if (err) console.log(err);
      const person = JSON.parse(bdy);
      console.log(person.name);
    });
  }
});
