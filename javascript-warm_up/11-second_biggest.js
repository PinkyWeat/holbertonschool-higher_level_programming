#!/usr/bin/node
let len = process.argv.length;
let sorted = [];

while (len > 2) {
  len--; sorted.push(process.argv[len]);
} // copy paste of given nums

sorted = sorted.sort((a, b) => a - b); // sorting for easier comparison
console.log(sorted);
const res = sorted[sorted.length - 2]; // process.argv.length - 4 works
console.log(res);
