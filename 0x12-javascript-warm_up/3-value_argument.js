#!/usr/bin/node

const proc = process.argv;

if (proc[2] === undefined) {
  console.log('No argument');
} else {
  console.log(proc[2]);
}
