#!/usr/bin/node

const proc = process.argv;
const checked = parseInt(proc[2]);
let x, y;

if (isNaN(checked)) {
  console.log('Missing size');
} else {
  for (x = 0; x < checked; x++) {
    console.log('X');
  for (y = 0; y < checked-1; y++) {
      console.log('X');
  }
  }
}
