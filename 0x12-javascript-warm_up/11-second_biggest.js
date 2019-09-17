#!/usr/bin/node
const newA = process.argv;
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let i;
  for (i = 0; i < process.argv.length; i++) {
    newA[i] = parseInt(process.argv[i]);
  }
  console.log(newA.slice(2).sort(function (a, b) { return b - a; })[1]);
}
