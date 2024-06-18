#!/usr/bin/node
const process = require('process');

let argv = process.argv;

let argc = argv.length - 2;
let number = parseInt(argv[2]);

if (isNaN(number)) {
        console.log('Missing number of occurrences');
}

if (argc > 0 && !isNaN(number)) {
    let idx = 0;
    for (; idx < number ; idx++) {
        console.log('C is fun');
    }
}