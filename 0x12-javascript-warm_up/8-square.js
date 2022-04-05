#!/usr/bin/node
let Phrase = '';
const MyVar = process.argv[2];

if (parseInt(MyVar)) {
  for (let i = 0; i < MyVar; i++) {
    Phrase += 'X';
  }
  for (let j = 0; j < MyVar; j++) {
    console.log(Phrase);
  }
} else {
  console.log('Missing size');
}
