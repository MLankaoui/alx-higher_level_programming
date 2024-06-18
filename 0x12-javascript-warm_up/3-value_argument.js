#!/usr/bin/node
const process = require('process');

function len (arr) {
  let count = 0;
  while (arr[count] !== undefined) {
    count++;
  }

  return count;
}

const argv = process.argv;

const argc = len(argv) - 2;

if (argc === 0) {
  console.log('No argument');
}

if (argc > 0) {
  console.log(argv[2]);
}
