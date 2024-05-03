#!/usr/bin/node

const proc = process.argv[2];

if (Number(proc)) {
  console.log(`My number: ${Number(proc)}`);
} else {
  console.log('Not a number');
}
