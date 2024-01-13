#!/usr/bin/node

// Extract the command-line arguments and convert them to integers
const args = process.argv.slice(2).map(Number);

// Check if no arguments are passed or only one argument is passed
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  // Sort the array in descending order
  const sortedArgs = args.sort((a, b) => b - a);
  console.log(sortedArgs[1]);
}
