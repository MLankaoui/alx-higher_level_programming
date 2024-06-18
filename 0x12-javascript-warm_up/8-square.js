#!/usr/bin/node
const process = require('process');

const argv = process.argv;

const argc = argv.length - 2;

const number = parseInt(argv[2]);

if (isNaN(number)) {
  console.log('Missing size');
}

if (argc == 1 && !isNaN(number)) {
  let idx = 0;
  for (; idx < number; idx++) {
    console.log('x'.repeat(number));
  }
}

// let i, j;

//     i = 0;
//     j = 0;
//     for (; i < number; i++) {
//         for (; j < number; j++) {
//             console.log("x".repeat(number));
//         {
//     }
