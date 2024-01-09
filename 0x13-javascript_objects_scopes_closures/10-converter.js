#!/usr/bin/node
// Converts a number from base10 to to another base
exports.converter = function (base) {
	return function (num) {
		return num.toString(base);
	};
};
