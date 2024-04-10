#!/usr/bin/node

const proc = process.argv;
const checked = parseInt(proc[2]);

if (isNaN(checked)) {
  console.log('Not a Number');
} else {
  console.log('My number: ' + checked);
}
