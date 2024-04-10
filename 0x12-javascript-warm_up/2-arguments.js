#!/usr/bin/node

const proc = process.argv;

if (proc.length < 3) {
  console.log('No arguement');
} else if (proc.length === 3) {
  console.log('Arguement found');
} else {
  console.log('Arguements found');
}
