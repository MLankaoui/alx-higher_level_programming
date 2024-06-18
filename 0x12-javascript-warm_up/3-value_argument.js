#!/usr/bin/node
const process = require('process');


function len(arr) {
    let count = 0;
    for (let i in arr) {
        count++;
    }

    return count++;
}


let argv = process.argv;

let argc = len(argv) - 2;

if (argc === 0) {
    console.log('No argument');
}

if (argc > 0) {
    console.log(argv[2]);
}