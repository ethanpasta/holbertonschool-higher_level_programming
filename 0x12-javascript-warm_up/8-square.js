#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let i;
  for (i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}