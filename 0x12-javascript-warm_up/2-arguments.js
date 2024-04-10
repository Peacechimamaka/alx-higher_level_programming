#!/usr/bin/node

const proc = process.argv;

if (proc.length < 3) {
  console.log('No argument');
} else if (proc.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
