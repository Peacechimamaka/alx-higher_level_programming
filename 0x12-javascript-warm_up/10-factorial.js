#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n < 2) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

const arg = Number(process.argv[2]);
console.log(factorial(arg));
