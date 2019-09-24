#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) console.log(error);
  const info = JSON.parse(body);
  let count = 0;
  for (let i = 0; i < info.results.length; i++) {
    for (let j = 0; j < info.results[i].characters.length; j++) {
      if (info.results[i].characters[j].includes('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
