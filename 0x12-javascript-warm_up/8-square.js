#!/usr/bin/node

const proc = process.argv;
const checked = parseInt(proc[2]);

if (isNaN(checked)) {
	console.log('Missing size');
} else {
	let count = checked;
	while(count > 0) {
		console.log('X'.repeat(checked))
		count--;
	}
}
