#!/usr/bin/node
const MyVar = process.argv[2];

if (parseInt(MyVar)) {
  for (let i = 0; i < MyVar; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
