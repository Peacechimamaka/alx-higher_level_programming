#!/usr/bin/node
//script that reads and prins the content of a file.

const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', function (error, content) {
	console.log(error || content);
});
