#!/usr/bin/node
// Returns status code
let id = process.argv[2];
let url = `https://swapi.dev/api/films/${id}`;
const request = require('request');

request(url, function (err, response, body) {
	if (err) {
		console.log(err);
		return;
	}

	if (response.statusCode === 200) {
		try {
			body = JSON.parse(body);
			console.log(body['title']);
		} catch (parseError) {
			console.log('Error parsing JSON:', parseError);
		}
	} else {
		console.log('Error code:', response.statusCode);
	}
});
