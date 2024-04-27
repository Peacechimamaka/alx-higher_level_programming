#!/usr/bin/node

function add(a, b) {
let result;
const proc = process.argv;
a = parseInt(proc[2]);
b = parseInt(proc[3]);
console.log(a);
if (isNaN(a) ||  isNaN(b)){
  console.log(NaN);
} else {
  result = a + b;
  console.log(result);
}
}
add(a, b);
