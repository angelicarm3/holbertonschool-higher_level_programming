#!/usr/bin/node

function factorial (number) {
  let Result = 1;
  for (let i = 1; i <= number; i++) {
    Result *= i;
  }
  return (Result);
}
console.log(factorial(parseInt(process.argv[2])));
