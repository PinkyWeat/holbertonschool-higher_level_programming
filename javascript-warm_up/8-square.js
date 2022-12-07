#!/usr/bin/node
if (parseInt(process.argv[2])) {
  let size = process.argv[2];
  let concat = '';
  while (size > 0) {
    concat += 'X'; size--;
  }
  while (size < process.argv[2]) {
    console.log(concat); size++;
  }
} else {
  console.log('Missing size');
}
