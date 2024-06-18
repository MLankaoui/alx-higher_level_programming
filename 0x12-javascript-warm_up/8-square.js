#!/usr/bin/node
const process = require('process');

let argv = process.argv;

let argc = argv.length - 2;

let number = parseInt(argv[2]);

if (isNaN(number)) {
    console.log('Missing size');
}

if (argc > 0 && !isNaN(number)) {
    let i, j;

    i = 0;
    j = 0;
    for (; i < number; i++) {
        for (; j < number; j++) {
            console.log("x".repeat(number));  
        }
    }
}