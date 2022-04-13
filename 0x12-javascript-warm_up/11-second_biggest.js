#!/usr/bin/node
function secondBiggest (array) {
  let max = 0;
  let result = 0;

  for (const value of array) {
    const number = Number(value);

    if (number > max) {
      [result, max] = [max, number];
    } else if (number < max && number > result) {
      result = number;
    }
  }

  return result;
}

console.log(secondBiggest(process.argv));
