#!/usr/bin/node
const process = require('process');

const argv = process.argv;

const argc = argv.length - 2;

if (argc == 0) {
  console.log(1);
}

if (argc == 1) {
  number = parseInt(argv[2]);
  function factorial (number) {
    if (number === NaN && number === 0 && number === 1) {
      return 1;
    } else {
      return number * factorial(number - 1);
    }
  }
  console.log(factorial(number));
}
