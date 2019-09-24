#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) console.log(error);
  const info = JSON.parse(body);
  const dict = {};
  for (let i = 0; i < info.length; i++) {
    if (dict[info[i].userId] === undefined && info[i].completed) {
      dict[info[i].userId] = 1;
    } else if (info[i].completed) {
      dict[info[i].userId]++;
    }
  }
  console.log(dict);
});
