#!/usr/bin/node
const process = require('process');

let argv = process.argv;

let argc = argv.length - 2;


console.log(argc);
function add(argv, argc) {
    if (argc != 2) {
        console.log(NaN);
    }

    else {
        console.log(parseInt(argv[2]) + parseInt(argv[3]));
    }
}

add(argc, argv);