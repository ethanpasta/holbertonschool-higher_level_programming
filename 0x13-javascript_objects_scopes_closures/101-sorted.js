#!/usr/bin/node
const dict = require('./101-data').dict;
const newdict = {};
for (var key in dict) {
  const val = dict[key];
  if (newdict[val] === undefined) {
    newdict[val] = [key];
  } else {
    newdict[val].push(key);
  }
}
console.log(newdict);
