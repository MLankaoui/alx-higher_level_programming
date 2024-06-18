#!/usr/bin/node
const process = require('process');

const argv = process.argv;

const argc = argv.length - 2;

if (argc !== 2) {
  console.log(NaN);
} else {
  const numberOne = parseInt(argv[2]);
  const numberTwo = parseInt(argv[3]);

  function add (a, b) {
    return a + b;
  }

  console.log(add(numberOne, numberTwo));
}
