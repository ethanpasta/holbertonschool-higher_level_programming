#!/usr/bin/node
function fact (n) {
  if (isNaN(n) || n === 1 || n === 0) {
    return 1;
  } else {
    return fact(n - 1) * n;
  }
}
const num = parseInt(process.argv[2]);
console.log(fact(num));
