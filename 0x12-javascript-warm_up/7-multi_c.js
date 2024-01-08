#!/usr/bin/node
// A script to print C is fun by the number of the argument
const  numOccurance = parseInt(process.argv[2]);

if (!isNaN(numOccurance) && numOccurance > 0) {
	for (let i = 0; i < numOccurance; i++) {
		console.log("C is fun");
	}
} else {
	console.log("Missing number of occurrences")
}
