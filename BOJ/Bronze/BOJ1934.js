// https://www.acmicpc.net/problem/1934

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");
const T = Number(input[0]);

const getGcd = (a, b) => {
  if (b === 0) {
    return a;
  }
  return getGcd(b, a % b);
}

const getLcm = (a, b) => {
  return (a * b) / getGcd(a, b);
}

for (let i = 1; i < T+1; i++) {
  const [A, B] = input[i].trim().split(" ").map(Number);
  const lcm = getLcm(A, B);
  console.log(lcm);
}