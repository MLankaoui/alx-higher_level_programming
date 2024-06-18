#!/usr/bin/node
const process = require('process');

const argv = process.argv;

const argc = argv.length - 2;

if (argc === 0) {
  console.log(1);
}

if (argc === 1) {
  const number = parseInt(argv[2]);
  function factorial (number) {
    if (isNaN(number)) {
      return 1;
    } else if (number === 1) {
      return 1;
    } else {
      return number * factorial(number - 1);
    }
  }
  console.log(factorial(number));
}
