#!/usr/bin/node
// a script to print the contents of a webpage and stores it in a file.
let url = process.argv[2];
let filename = process.argv[3];
const fs = require('fs');
const request = require('request');

request(url, function (err, response, body) {
	if (err) {
		console.log(err);
	} else {
		fs.writeFile(filename, body, function(err) {
			if (err) {
				console.log(err);
			}
		});
	}
});
