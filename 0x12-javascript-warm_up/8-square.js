#!/usr/bin/node

const proc = process.argv;
const checked = Number(proc[2]);

if (!checked) {
  console.log('Missing size');
} else {
  let count = checked;

  while (count > 0) {
    console.log('X'.repeat(checked));
    count--;
  }
}
