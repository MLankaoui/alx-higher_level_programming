#!/usr/bin/node
const process = require('process');

const argv = process.argv;

const argc = argv.length - 2;

if (argc < 2) {
  console.log(0);
} else {
  let largest = parseInt(argv[2]);
  let secondLargest = -Infinity;

  for (let i = 3; i < argc + 2; i++) {
    const num = parseInt(argv[i]);
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num < largest) {
      secondLargest = num;
    }
  }

  console.log(secondLargest);
}
