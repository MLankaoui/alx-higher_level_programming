#!/usr/bin/node
const process = require('process');

let argv = process.argv;

let toInt = Math.floor(argv[2])

if (isNaN(toInt)) {
    console.log('Not a number');
}

else {
    console.log(toInt);
}