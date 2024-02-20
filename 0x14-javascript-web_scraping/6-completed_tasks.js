#!/usr/bin/node
const request = require('request');

let apiURL = process.argv[2];

request(apiURL, function(error, response, body) {
	if (error) {
		console.error(error);
		return;
	}

	if (response.statusCode !== 200) {
		console.error('Error:', response.statusCode);
		return;
	}

	let completedTasks = {};
	// Parse JSON response
	let todos = JSON.parse(body);

	// Iterate through todos
	todos.forEach(function(todo) {
		// Check if task is completed
		if (todo.completed) {
			// Increment count for user ID
			if (completedTasks[todo.userId] === undefined) {
				completedTasks[todo.userId] = 1;
			} else {
				completedTasks[todo.userId]++;
			}
		}
	});

	// Print completed tasks by uer ID
	console.log(completedTasks);
});
