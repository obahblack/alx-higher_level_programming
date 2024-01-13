#!/usr/bin/node

const Rectangle = require(`./4-rectangle`);

module.exports = class Square extends Rectangle {
	constructor (size) {
		// Call the constructor of parent class (Rextangle)
		super(size, size);
	}
};
