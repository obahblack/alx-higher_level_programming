#!/usr/bin/node
// This script converts argument to int
const numConv = parseInt(process.argv[2]);
if (!isNaN(numConv)) {
	console.log(`My number: ${numConv}`);
} else {
	console.log("Not a number");
}
