#!/usr/bin/node

const numOccurrences = process.argv[2];

if (!numOccurrences || isNaN(numOccurrences) || numOccurrences <= 0) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numOccurrences; i++) {
    console.log('C is fun');
  }
}
