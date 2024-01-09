#!/usr/bin/node

module.exports = class Rectangle {
	constructor (w, h) {
		// Create an empty object if w or h is not a positive integer
		if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
			return {};
		}
		this.width = w;
		this.height = h;
	}
}
