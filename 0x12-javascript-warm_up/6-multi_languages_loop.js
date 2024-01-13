#!/usr/bin/node
// Script that prints 3 lines but using an array of string and a loop
let array = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

// Here array. values() method is called.
let things = array.values();
for (let elements of things) {
	console.log(elements);
}
