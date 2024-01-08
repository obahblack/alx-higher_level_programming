#!/usr/bin/node
// Script that prints a square (equal width and height)
const size = parseInt(process.argv[2]);
if (!isNaN(size) && size > 0) {
	for (let i = 0; i < size; i++) {
		console.log('X'.repeat(size));
	}
} else {
	console.log("Missing size");
}
