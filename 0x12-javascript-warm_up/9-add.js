#!/usr/bin/node
const process = require('process');

let argv = process.argv;

let argc = argv.length - 2;

if (argc != 2) {
    console.log(NaN);
}

else {
    let number_one = parseInt(argv[2]);
    let number_two = parseInt(argv[3]);

    function add(a, b) {
        return a + b;
    }

    console.log(add(number_one, number_two));
}