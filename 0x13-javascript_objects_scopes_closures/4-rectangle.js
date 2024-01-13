#!/usr/bin/node

module.exports = class Rectangle {
	constructor(w, h) {
		if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
                return {};
        }
                this.width = w;
                this.height = h;
	}

	print() {
		// Print the rectangle using X
		for (let col = 0; col < this.height; col++) {
			console.log('X'.repeat(this.width));
		}
	}

	rotate() {
		// This side rotates the values or swap
		[this.width, this.height] = [this.height, this.width];
	}

	double() {
		// Double the width and height
		this.width *= 2;
		this.height *= 2;
	}
}
