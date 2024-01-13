#!/usr/bin/node
// A script to compute and print a factorial
const number = parseInt(process.argv[2]);

// Define the factorial function
function factorial(n) {
	if (isNaN(n)){
		return 1;
	} else if (n === 0) {
		return 1;
	} else {
		return (n * factorial(n -1));
	}
}
console.log(factorial(number));
