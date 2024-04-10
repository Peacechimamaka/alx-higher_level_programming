#!/usr/bin/node

const proc = process.argv;
const checked = parseInt(proc[2]);
let x;

if (isNaN(checked)) {
  console.log('Missing number of occurrences');
} else {
  for (x = 0; x < checked; x++) {
    console.log('C is fun');
  }
}
