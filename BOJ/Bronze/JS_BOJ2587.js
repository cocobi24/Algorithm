const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);

const avg = input.reduce(function add(sum, currValue) {
  return sum + currValue;
}, 0);

const mid = input.slice();
mid.sort(function(a, b)  {
  return a - b;
});

console.log(avg/5);
console.log(mid[2]);