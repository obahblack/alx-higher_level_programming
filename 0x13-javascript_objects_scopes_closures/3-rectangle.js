#!/usr/bin/node

module.exports = class Rectangle {
	constructor(w, h) {
		if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
			return {};
		}

		this.width = w;
		this.height = h;
	}

	// Prints the rectangle using the character
	print () {
		for (let col = 0; col < this.height; col++) {
			console.log('X'.repeat(this.width));
		}
	}
}
