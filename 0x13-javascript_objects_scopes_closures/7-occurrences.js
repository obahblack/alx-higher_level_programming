#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
	let num = 0;
	for (let i in list) {
		if (list[i] === searchElement) {
			num++;
		}
	}
	return num;
};
