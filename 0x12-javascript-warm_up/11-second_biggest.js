#!/usr/bin/node

const args = process.argv.slice(2);
const n = args.length;

if (n <= 1) {
  console.log(0);
} else {
  let max1 = parseInt(args[0]);
  let max2 = parseInt(args[1]);
  if (max2 > max1) {
    [max1, max2] = [max2, max1];
  }
  for (let i = 2; i < n; i++) {
    const x = parseInt(args[i]);
    if (x > max1) {
      max2 = max1;
      max1 = x;
    } else if (x > max2) {
      max2 = x;
    }
  }
  console.log(max2);
}
