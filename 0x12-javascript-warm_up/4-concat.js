#!/usr/bin/node

const proc = process.argv;

if ((proc[2] === undefined) && (proc[3] === undefined)) {
  console.log('undefined is undefined');
} else {
  console.log(proc[2] + ' is ' + proc[3]);
}
