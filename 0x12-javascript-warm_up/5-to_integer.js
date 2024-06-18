#!/usr/bin/node
const process = require('process');

const argv = process.argv;

const toInt = Math.floor(argv[2]);

if (isNaN(toInt)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + toInt);
}
