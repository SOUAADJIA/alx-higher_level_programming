#!/usr/bin/node

const numOccu = process.argv[2];

if (!numOccu || isNaN(numOccu) || numOccu <= 0) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numOccu; i++) {
    console.log('C is fun');
  }
}
