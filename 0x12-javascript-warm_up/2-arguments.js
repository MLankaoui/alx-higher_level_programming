#!/usr/bin/node
// including the process module
const process = require('process');
let argc = process.argv.length - 2;

if (argc == 0)
{
    console.log("No argument");
}

else if (argc == 1)
{
    console.log('Argument found');
}

else if (argc > 1)
{
    console.log('Arguments found')    
}    